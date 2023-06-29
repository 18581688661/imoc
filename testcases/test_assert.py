import pytest
from pytest_assume.plugin import assume


class TestAssert:
    def test_assert(self):
        # assert "william"!="william"
        # assert "william" == "william"
        # assert "william" in "william ueiwueiwuie"
        # assert False

        pytest.assume(1 + 2 == 3)
        assert 1 + 1 == 2
        with assume: assert 3 > 2
        with assume: assert "ab" in "ab ss"
        print("结束")
