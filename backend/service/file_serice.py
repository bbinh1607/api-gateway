from backend.service.base_service import BaseService
from backend.config import Config

class FileService(BaseService):
    def __init__(self, path, method, data=None, params=None, is_public=False, files=None):
        super().__init__(Config.FILE_SERVICE_URL, path, method, data=data, params=params, is_public=is_public, files=files)