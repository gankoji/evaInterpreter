from eva import *

eva = Eva()

def test_eva():
    assert True

def test_number():
    assert eva.eval(2) == 2

def test_string():
    assert eva.eval('"HALLO"') == 'HALLO'

def test_var():
    assert eva.eval(['var', 'hi', 1]) == 1

def test_add():
    assert eva.eval(['+', 1, ['+', 1, 2]]) == 4

def test_sub():
    assert eva.eval(['-', ['+', 1, 2], 1]) == 2

def test_mult():
    assert eva.eval(['*', 2, 3]) == 6

def test_div():
    assert eva.eval(['/', 6, 2]) == 3

def test_varAccess():
    eva.eval(['var', 'x', 10])
    assert eva.eval(['x']) == 10

def test_block():
    assert eva.eval(
        ['begin',
            ['var', 'x', 10],
            ['var', 'y', 20],
            ['+', ['*', 'x', 'y'], 30],
        ]) == 230