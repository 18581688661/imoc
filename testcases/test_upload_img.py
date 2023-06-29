from common.tools import sep, getprojectpath
from urllib3 import encode_multipart_formdata
from common.common_requests import Requests
import allure


class Testimg:
    @allure.description("上传头像")
    @allure.epic("主流程")
    @allure.feature("上传头像")
    def test_upload_img(self, gettoken):
        img_path = getprojectpath() + sep(["img", "luffy.jpg"], add_sep_before=True)
        file_data = {"file": ("upload_img", open(img_path, "rb").read())}
        encode_data = encode_multipart_formdata(file_data)
        # print(encode_data)
        data = encode_data[0]
        # print(data)
        headers = {
            "token": gettoken("william"),
            "Content-Type": encode_data[1]
        }
        res = Requests(headers).post("/api/user/upload_head_img", data=data)
        print(res.text)
        assert res.json()["code"] == 200
