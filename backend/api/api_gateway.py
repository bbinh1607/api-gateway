from flask import Blueprint, request
from backend.service.device_service import DeviceService
from backend.service.identity_service import IdentityService
from backend.config import Config
from backend.middleware.auth_middleware import authenticate

getway_bp = Blueprint("getway", __name__)

@getway_bp.route(f'{Config.API_PREFIX}/device/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@authenticate()
def handle_device_request(path):
    data = request.get_json() if request.is_json else None
    params = request.args.to_dict()
    device_service = DeviceService(path,request.method, data, params)
    return device_service.execute().json()

@getway_bp.route(f'{Config.API_PREFIX}/identity/public/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_device_public_request(path):
    data = request.get_json() if request.is_json else None
    params = request.args.to_dict()
    identity_service = IdentityService(f"public/{path}", request.method, data, params)
    return identity_service.execute().json()

@getway_bp.route(f'{Config.API_PREFIX}/identity/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@authenticate()
def handle_identity_request(path):
    data = request.get_json() if request.is_json else None
    params = request.args.to_dict()
    identity_service = IdentityService(f"{path}", request.method, data, params)
    return identity_service.execute().json()