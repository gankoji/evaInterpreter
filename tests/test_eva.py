from ..eva.eva import *

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

def test_assignment():
    assert eva.eval(
        ['begin',
            ['var', 'data', 10],
            ['begin',
                ['set', 'data', 100]
            ],
            'data'
        ]
    ) == 100

def test_if():
    assert eva.eval(
        ['begin',
            ['var', 'x', 10],
            ['var', 'y', 0],

            ['if', ['>', 'x', 10],
                ['set', 'y', 20],
                ['set', 'y', 30]
            ],
            'y'
        ]
    ) == 30

def test_while():
    assert eva.eval(
        ['begin',
            ['var', 'counter', 0],
            ['var', 'result', 0],
            ['while', ['<', 'counter', 10],
                # result++
                # TODO: implement ['++', <Exp>]
                ['begin',
                    ['set', 'result', ['+', 'result', 1]],
                    ['set', 'counter', ['+', 'counter', 1]]
                ]
            ],
            'result'
        ]
    )