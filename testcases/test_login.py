import time

import pytest

from common.common_requests import Requests


class TestApi:
    # @pytest.mark.timeout(1)
    def test_login(self):
        data = {
            "user": "william",
            "password": 123456
        }
        # time.sleep(2)
        res = Requests().post("/api/user/login", json=data)

        print("token为", res.json()["data"]["token"])
