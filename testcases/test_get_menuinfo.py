from common.common_requests import Requests


class TestApi:
    def test_getmenuinfo(self, gettoken):
        # login_data = {
        #     "user": "william",
        #     "password": 123456
        # }
        # login_res = Requests().post("/api/user/login", json=login_data)
        # token = login_res.json()["data"]["token"]
        headers = {
            "token": gettoken('jay')
        }
        res = Requests(headers).get('/api/router/router_list')
        print(res.text)