import pytest
from arcchivo_funciones import*

@pytest.mark.parametrize("abc, string, resp",[
    ("a","nazareno", True),
    ("t","thomas", True),
    ("w","ruth", True),
])
def test_letterinstring(abc, string, resp):
    assert letterinstring(abc, string)==resp

@pytest.mark.parametrize("array, resp",[
    (("a","b","n"), "abc"),
    (("a","t","c"), "atc"),
    (("a","b","c"), "abc")
])
def test_arraystring(array,resp):
    assert arraystring(array)==resp

@pytest.mark.parametrize("strin,resp",[
    ("abc", ("a","b","n")),
    ("atc", ("a","m","c")),
])
def test_strarrays(strin,resp):
    assert strarrays(strin)==resp

