from requests.adapters import HTTPAdapter
from urllib.parse import urljoin
import requests
from flask import g
from werkzeug.datastructures import FileStorage

class BaseService:
    def __init__(self, base_url, path, method, data=None, params=None, is_public=False, files=None):
        self.method = method.upper()
        self.is_public = is_public
        self.url = urljoin(base_url, f"/{path}")
        self.data = data or {}
        self.params = params or {}
        self.files = files or None

        self.headers = {}
        # Remove Content-Type header when files are present
        if not self.files:
            self.headers["Content-Type"] = "application/json"

        if not self.is_public and hasattr(g, 'token') and g.token:
            self.headers["Authorization"] = f"Bearer {g.token}"

        self.session = requests.Session()

    def _prepare_files_for_requests(self):
        """Prepares the FileStorage objects for the requests library."""
        prepared_files = {}
        if self.files:
            for key, file_storage in self.files.items():
                if isinstance(file_storage, FileStorage):
                    prepared_files[key] = (
                        file_storage.filename,
                        file_storage.stream,
                        file_storage.content_type
                    )
                else:
                    # Handle cases where the value might not be a FileStorage object
                    prepared_files[key] = file_storage
        return prepared_files

    def execute(self):
        try:
            if self.method == "GET":
                response = self.session.get(self.url, headers=self.headers, params=self.params, timeout=10)
            elif self.method == "POST":
                # Prepare files correctly before sending
                if self.files:
                    prepared_files = self._prepare_files_for_requests()
                    response = self.session.post(self.url, headers=self.headers, data=self.data, files=prepared_files, timeout=10)
                else:
                    response = self.session.post(self.url, headers=self.headers, json=self.data, timeout=10)
            elif self.method == "PUT":
                response = self.session.put(self.url, headers=self.headers, json=self.data, timeout=10)
            elif self.method == "DELETE":
                response = self.session.delete(self.url, headers=self.headers, timeout=10)
            else:
                raise ValueError("Unsupported HTTP method")
            
            if response.status_code == 500:
                return response

            return response

        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the request: {e}")