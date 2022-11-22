from ..eva.environment import *

env = Environment()

def test_define():
    assert env.define('testOne', 5) == 5

def test_lookup():
    env.define('myTestVar', 5)
    assert env.lookup('myTestVar') == 5

def test_assign():
    env.assign('myTestVar', 20)
    assert env.lookup('myTestVar') == 20
