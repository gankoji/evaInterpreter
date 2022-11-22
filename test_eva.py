from eva import *

eva = Eva()

def test_eva():
    assert True

def test_number():
    assert eva.eval(2) == 2

def test_string():
    assert eva.eval("HALLO") == 'HALLO'