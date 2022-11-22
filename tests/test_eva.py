from ..eva.eva import *
from . import testUtils

eva = Eva()

def test_number():
    testUtils.test(eva,"2", 2)

def test_string():
    testUtils.test(eva, '"HALLO"', 'HALLO')

def test_add():
    testUtils.test(eva,
    """
        (+ 1 (+ 1 2))
    """, 4)

def test_sub():
    testUtils.test(eva,
    """
        (- (+ 1 2) 1)
    """, 2)

def test_mult():
    testUtils.test(eva, "(* 2 3)", 6)

def test_div():
    testUtils.test(eva, "(/ 6 2)", 3)

def test_var():
    testUtils.test(eva, "(var 'hi' 1)", 1)

def test_varAccess():
    testUtils.test(eva,
    """
        (begin (var 'x' 10)
        ('x'))
    """, 10)
    #eva.eval(['var', 'x', 10])
    #assert eva.eval(['x']) == 10

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

def test_testUtils():
    testUtils.test(eva, """
        (begin
            (var x 10)
            (var y 20)
            (+ (* x 10) y))
    """, 120)
