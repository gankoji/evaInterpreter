from ..parser import evaParser
def test(eva, code, expected):
    exp = evaParser.parse(code)
    assert eva.eval(exp) == expected
