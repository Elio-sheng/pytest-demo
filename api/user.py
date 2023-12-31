import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class UserService(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(UserService, self).__init__(api_root_url, **kwargs)

    def webUserLogin(self, **kwargs):
        return self.post("/user/web/sign/in", **kwargs)

    def thirdUserLogin(self, **kwargs):
        return self.post("/user/web/sign/in/third", **kwargs)

    def webRegister(self, **kwargs):
        return self.post("/user/web/sign/up", **kwargs)


userservice = UserService(api_root_url)
