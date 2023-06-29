from common.common_requests import Requests
import allure


class TestApi:
    @allure.description("获取钱包信息")
    @allure.epic("主流程")
    @allure.feature("获取钱包信息")
    def test_get_wallet_info(self, gettoken, get_balance_from_db):
        # login_data = {
        #     "user": "william",
        #     "password": 123456
        # }
        with allure.step("登录"):
            headers = {
                "token": gettoken("jay")
            }
        # 原方法
        # login_res = Requests().post("/api/user/login", json=login_data)
        # token = login_res.json()["data"]["token"]
        with allure.step("调用获取钱包信息接口"):
            res = Requests(headers).post('/api/wallet/get_wallet_info')
            print(res.text)
        with allure.step("断言"):
            assert res.json()["code"] == 200
            assert res.json()["data"]["balance"] == get_balance_from_db
