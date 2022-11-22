import re

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
            return exp[1:-1]

        #----------------------------
        # Math operations
        if (exp[0] == '+'):
            return self.eval(exp[1], env) + self.eval(exp[2], env)

        if (exp[0] == '-'):
            return self.eval(exp[1], env) - self.eval(exp[2], env)

        if (exp[0] == '*'):
            return self.eval(exp[1], env) * self.eval(exp[2], env)

        if (exp[0] == '/'):
            return self.eval(exp[1], env) / self.eval(exp[2], env)

        #----------------------------
        # Blocks  
        if (exp[0] == 'begin'):
            blockEnv = Environment({}, self.env)
            return self._evalBlock(exp, blockEnv)
        
        #---------------------------
        # Variable declaration
        if (exp[0] == 'var'):
            _, name, value = exp
            return self.env.define(name, self.eval(value))

        #---------------------------
        # Variable access
        if (self._isVariableName(exp[0])):
            return self.env.lookup(exp[0])

        raise TypeError(f'This type of expression is not yet implemented: {exp}')

    def _evalBlock(self, block, env):
        [_tag, *expressions] = block

        results = [self.eval(exp, env) for exp in expressions]
        return results[-1]

    def _isNumber(self, exp):
        return (type(exp) == int) or (type(exp) == float)

    def _isString(self, exp):
        return (type(exp) == str) and (exp[0] == '"') and (exp[-1] == '"')

    def _isVariableName(self, exp):
        return (type(exp) == str) and (re.search(r"^[+\-*/<>=a-zA-Z0-9_]+$", exp))
