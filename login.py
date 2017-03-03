
import unittest
import requests
import json

class Login(unittest.TestCase):
    def setUp(self):
        self.url="http://172.16.0.60:8811/services/sys/login.json"
        self.headers={"Content-Type": "application/json"}
        self.data={"reqHead": { "reqSn": "10001","reqTime": "20151223173601","apiName": "investigation.wise.sys.login","deviceId": "见'reqHead说明.json'"},
             "userSource": "1","username": "li1","password": "11"}
    def test_login(self):
        res=requests.post(self.url,data=json.dumps(self.data),headers=self.headers)
        print(res.text)
        self.assertEqual(res.status_code,200)


if __name__ == '__main__':
    unittest.main()


