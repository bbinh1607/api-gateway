import requests
from backend.config import Config

def verify_token(token):
    url = f"{Config.IDENTITY_SERVICE_URL}/auth/verify-token"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.post(url, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('data')
        else:
            return {"error": response.json().get("message", "Unknown error")}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

