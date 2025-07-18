from functools import wraps
from flask import request, jsonify, g
import jwt
from backend.utils.token_helper.verify_token import verify_token

def authenticate(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Lấy token từ header Authorization
            token = request.headers.get('Authorization')
            
            # Nếu không có token, trả về lỗi Unauthorized
            if not token:
                return jsonify({"error": "Token is missing"}), 401

            try:
                token = token.replace("Bearer ", "")
                
                decoded_token = verify_token(token)

                if role and role != decoded_token.get('role'):
                    return jsonify({"error": "Unauthorized, insufficient role"}), 403

                g.user = decoded_token
                g.token = token

            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Invalid token"}), 401

            return f(*args, **kwargs)  # Tiếp tục xử lý request nếu token hợp lệ

        return wrapper
    return decorator
