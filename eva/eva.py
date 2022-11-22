import re

from .environment import *

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
            print("We think this is a string")
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
        # Comparison operators
        if (exp[0] == '>'):
            return this.eval(exp[1], env) > this.eval(exp[2], env)

        if (exp[0] == '>='):
            return this.eval(exp[1], env) >= this.eval(exp[2], env)

        if (exp[0] == '<'):
            return this.eval(exp[1], env) < this.eval(exp[2], env)

        if (exp[0] == '<='):
            return this.eval(exp[1], env) <= this.eval(exp[2], env)

        if (exp[0] == '='):
            return this.eval(exp[1], env) == this.eval(exp[2], env)

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
        # Variable assignment
        if (exp[0] == 'set'):
            _, name, value = exp
            return self.env.assign(name, value)

        #---------------------------
        # Variable access
        if (self._isVariableName(exp) or self._isVariableName(exp[0])):
            print(f'We think this is a variable: {exp}')
            if type(exp) == list:
                return self.env.lookup(exp[0])
            else:
                return self.env.lookup(exp)

        raise TypeError(f'This type of expression is not yet implemented: {exp}')

    def _evalBlock(self, block, env):
        print("Evaluating a block")
        [_tag, *expressions] = block

        results = [self.eval(exp, env) for exp in expressions]
        return results[-1]

    def _isNumber(self, exp):
        return (type(exp) == int) or (type(exp) == float)

    def _isString(self, exp):
        return (type(exp) == str) and (exp[0] == '"') and (exp[-1] == '"')

    def _isVariableName(self, exp):
        return (type(exp) == str) and (re.search(r"^[+\-*/<>=a-zA-Z0-9_]+$", exp))

if __name__ == "__main__":
    eva = Eva()
    eva.eval(
        ['begin',
            ['var', 'data', 10],
            ['begin',
                ['set', 'data', 100]
            ],
            'data'
        ]
    )