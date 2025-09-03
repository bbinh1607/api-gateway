from backend.service.base_service import BaseService
from backend.config import Config

class IdentityService(BaseService):
    def __init__(self, path, method, data=None, params=None, is_pubic = False):
        super().__init__(Config.IDENTITY_SERVICE_URL, path, method, data, params, is_pubic)