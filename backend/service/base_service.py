from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin
import requests
from flask import g

class BaseService:
    def __init__(self, base_url, path, method, data=None, params=None):
        self.method = method.upper()
        self.url = urljoin(base_url, f"/{path}")
        self.data = data or {}
        self.params = params or {}

        self.headers = {
            "Content-Type": "application/json"
        }

        if hasattr(g, 'token') and g.token:
            self.headers["Authorization"] = f"Bearer {g.token}"

        # Retry logic
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session = requests.Session()
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def execute(self):
        if self.method == "GET":
            return self.session.get(self.url, headers=self.headers, params=self.params, timeout=10)
        elif self.method == "POST":
            return self.session.post(self.url, headers=self.headers, json=self.data, timeout=10)
        elif self.method == "PUT":
            return self.session.put(self.url, headers=self.headers, json=self.data, timeout=10)
        elif self.method == "DELETE":
            return self.session.delete(self.url, headers=self.headers, timeout=10)
        else:
            raise ValueError("Unsupported HTTP method")
