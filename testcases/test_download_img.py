import requests
import allure
from common.yamlconfig import getprojectpath, sep


class TestDownload:
    @allure.description("下载图片")
    @allure.epic("主流程")
    @allure.feature("下载图片")
    def test_download_img(self, gettoken):
        headers = {
            "token": gettoken("william")
        }
        res = requests.get(
            "http://47.101.216.239:9090/product/product_img/168759362395323d05555-82ea-4985-9803-8c69497215c0",
            headers=headers)

        download_path = getprojectpath() + sep(["img", "download_img.jpg"], add_sep_before=True)
        with open(download_path, "wb") as f:
            f.write(res.content)
