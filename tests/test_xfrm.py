from ..eva.eva import *
from . import testUtils

eva = Eva()


def test_switch():
    testUtils.test(eva, 
    """
        (begin
            (var x 10)

            (switch ((= x 10) 100)
                    ((> x 10) 200)
                    (else 300))
        )
    """, 100)