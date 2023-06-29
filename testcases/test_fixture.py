import pytest


class TestPytest:

    @pytest.fixture(scope="function")
    def front(self):
        yield "https://"
        print("测试结束")

    @pytest.mark.bing
    def test_bing(self,front):
        print("bing", f"{front}www.bing.com")

    @pytest.mark.baidu
    def test_baidu(self,front):
        print("baidu", f"{front}www.baidu.com")
