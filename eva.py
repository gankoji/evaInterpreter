from environment import *

class Eva:
    def __init__(self, globalEnv = Environment()): 
        self.env = globalEnv

    def eval(self, exp, env = None):
        if env == None:
            env = self.env

        #----------------------------
        # Self-evaluating expressions
        if (self._isNumber(exp)):
            return exp

        if self._isString(exp):
            return exp
        
        raise UnimplementedError(f'This type of expression is not yet implemented: {exp}')

    def _isNumber(self, exp):
        return (type(exp) == int) or (type(exp) == float)

    def _isString(self, exp):
        return type(exp) == str
