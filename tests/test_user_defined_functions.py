from ..eva.eva import *
from . import testUtils

eva = Eva()

def test_udfs():
    testUtils.test(eva, 
    """
        (begin
            (def square (a)
                (* a a))
            (square 2)
        )
    """,4)

    testUtils.test(eva,
    """
        (begin
            (def calc (x y)
                (begin
                    (var z 30)
                    (+ (* x y) z)
                ))
            (calc 10 20)
        )
    """, 230)
