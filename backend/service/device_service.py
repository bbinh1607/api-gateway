from backend.service.base_service import BaseService
from backend.config import Config

class DeviceService(BaseService):
    def __init__(self, path, method, data=None, params=None):
        super().__init__(Config.DEVICE_SERVICE_URL, path, method, data, params)
