import pytest

from common.common_requests import Requests

goods = [
    {
        "product_title": "路飞手办NFT002",
        "product_stock": 1,
        "product_price": "19.99",
        "product_status": 1,
        "product_desc": "一个路飞手办NFT002",
        "product_img": [
            "http://47.101.216.239:9090/product/product_img/16871826978821850bf3f-7bcc-433d-b61e-354b32961f2c"
        ]
    },
    {
        "product_title": "路飞手办NFT003",
        "product_stock": 1,
        "product_price": "19.99",
        "product_status": 1,
        "product_desc": "一个路飞手办NFT003",
        "product_img": [
            "http://47.101.216.239:9090/product/product_img/16871826978821850bf3f-7bcc-433d-b61e-354b32961f2c"
        ]
    }
]


class TestApi:
    @pytest.mark.parametrize("goods_info", goods)
    # @pytest.mark.skip("无需执行")
    def test_add_product(self, gettoken, goods_info):
        headers = {
            "token": gettoken("william")
        }

        res = Requests(headers).post('/api/product/publish_product', json=goods_info)
        print(res.text)
        assert res.json()["code"] == 200
        assert res.json()["msg"] == "成功"
