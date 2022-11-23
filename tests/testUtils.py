from ..parser import evaParser
def test(eva, code, expected):
    exp = evaParser.parse(code)
    res = eva.eval(exp)
    if res != expected:
        print(f"This test failed. Expression: {exp}, result: {res}")
    assert eva.eval(exp) == expected
