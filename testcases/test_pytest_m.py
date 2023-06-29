import pytest


class TestPytest:
    @pytest.mark.bing
    def test_bing(self):
        print("bing", "http://www.bing.com")

    @pytest.mark.baidu
    def test_baidu(self):
        print("baidu", "http://www.baidu.com")
