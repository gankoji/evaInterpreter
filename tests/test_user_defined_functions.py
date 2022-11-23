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
