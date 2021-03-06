def tokenize(s):
    i, n = 0, len(s)
    while i < n:
        if s[i].isspace():
            i += 1
        elif s[i] in ['+', '-', '(', ')']:
            yield s[i]
            i += 1
        else:
            j = i + 1
            while j < n and s[j].isdigit():
                j += 1
            yield int(s[i:j])
            i = j

def eval_tokens(tokens):
    result = []
    opstack = []
    def pop_op():
        a2 = result.pop()
        a1 = result.pop()
        op = opstack.pop()
        if op == '+':
            result.append(a1 + a2)
        elif op == '-':
            result.append(a1 - a2)
        else:
            raise RuntimeError()
    for tok in tokens:
        if tok in ['+', '-']:
            while opstack and opstack[-1] != '(':
                pop_op()
            opstack.append(tok)
        elif tok == '(':
            opstack.append(tok)
        elif tok == ')':
            while opstack[-1] != '(':
                pop_op()
            assert opstack[-1] == '('
            opstack.pop()
        else:
            result.append(tok)
    while opstack:
        pop_op()
    return result[-1]

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval_tokens(tokenize(s))
