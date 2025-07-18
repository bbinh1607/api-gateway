from flask import Blueprint, request
from backend.service.device_service import DeviceService
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

@getway_bp.route(f'{Config.API_PREFIX}/device/public/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_device_public_request(path):
    data = request.get_json() if request.is_json else None
    params = request.args.to_dict()
    device_service = DeviceService(f"public/{path}", request.method, data, params)
    return device_service.execute().json()