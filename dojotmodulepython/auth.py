import requests
from .config import config
import base64
import json


class Auth:

    def __init__(self):
        self.a = "a"

    def getManagementToken(self):

        userinfo = {
            "username": "internal",
            "service": config.dojot["managementService"]
        }

        jwt = "{}.{}.{}".format(base64.b64encode("model".encode()).decode(),
                                base64.b64encode(json.dumps(
                                    userinfo).encode()).decode(),
                                base64.b64encode("signature".encode()).decode())

        return jwt

    def getTenants(self):
        url = config.auth['host'] + "/admin/tenants"

        ret = requests.get(
            url, headers={'Authorization': "Bearer " + self.getManagementToken()})


auth = Auth()
