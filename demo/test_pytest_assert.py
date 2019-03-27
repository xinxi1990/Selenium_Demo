import pytest

#assert可以使用直接使用“==”、“!=”、“<”、“>”、“>=”、"<=" 等符号来比较相等、不相等、小于、大于、大于等于和小于等于
class Testpytest():
    def test_assert_eq(self):
        assert 1 == 1

    def test_assert_ne(self):
        assert 1 != 1

    def test_assert_less(self):
        assert 1 >=1

