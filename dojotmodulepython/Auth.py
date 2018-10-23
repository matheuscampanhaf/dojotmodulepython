import requests
from .Config import config
import base64
import json

class Auth:

    def get_management_token(self, tenant):

        userinfo = {
            "username": tenant,
            "service": config.dojot["management_service"]
        }

        jwt = "{}.{}.{}".format(base64.b64encode("model".encode()).decode(),
                                base64.b64encode(json.dumps(
                                    userinfo).encode()).decode(),
                                base64.b64encode("signature".encode()).decode())

        return jwt

    def get_tenants(self):

        url = "http://172.20.0.17:5000" + "/admin/tenants"
        print(url)
        ret = requests.get(url, headers={'authorization': self.get_management_token(config.dojot['management_service'])})
        payload = ret.json()
        
        return payload['tenants']

auth = Auth()