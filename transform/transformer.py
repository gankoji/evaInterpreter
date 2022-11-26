
class Transformer:
    def __init__(self):
        self.isValid = True

    def transformDeftoLambda(self, exp):
        [_tag, name, params, body] = exp
        return ['var', name, ['lambda', params, body]]
    
    def transformSwitchToIf(self, exp):
        [_tag, *cases] = exp

        ifExp = ['if', None, None, None]

        current = ifExp

        for i in range(len(cases)):
            [currentCond, currentBlock] = cases[i]

            current[1] = currentCond
            current[2] = currentBlock
            
            next = cases[i+1]
            [nextCond, nextBlock] = next
            if nextCond == 'else':
                current[3] = nextBlock
                break
            else:
                current[3] = ifExp.copy()

            current = current[3]

        return ifExp