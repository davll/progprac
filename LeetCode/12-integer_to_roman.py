SYMBOLS = [
    [0, 'I', 'V', 'X'],
    [0, 'X', 'L', 'C'],
    [0, 'C', 'D', 'M'],
    [0, 'M', None, None]
]

def _i2r(x, m):
    table = SYMBOLS[m]
    if x == 0:
        return
    elif x <= 3: # I II III
        for _ in range(x):
            yield table[1]
    elif x == 4: # IV
        yield table[1]
        yield table[2]
    elif x <= 8: # V VI VII VIII
        yield table[2]
        for _ in range(x-5):
            yield table[1]
    elif x == 9: # IX
        yield table[1]
        yield table[3]
    else:
        raise ValueError()

def int2roman(num):
    from itertools import chain
    k1 = _i2r((num // 1000), 3)
    k2 = _i2r((num // 100) % 10, 2)
    k3 = _i2r((num // 10) % 10, 1)
    k4 = _i2r(num % 10, 0)
    return ''.join(chain(k1, k2, k3, k4))

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return int2roman(num)
