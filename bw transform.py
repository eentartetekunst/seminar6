''' C func сколько символов строки меньше, чем символ на входе'''

def cfunc(symbol, string):
    counter = 0
    if symbol == '$':
        counter = 0
    else:
        for i in range(len(string)):
            if str(string[i]) < symbol:
                counter += 1
    return counter

''' LFC  возвращает С(символ) + число этих символов в слове BWT от 1 до r'''

def lfc(symbol, r):
    c = cfunc(symbol)
    d = 0
    for i in range(r):
        if bwt(i, p) == symbol:
            d+=1
    return c + d

''' BWT  '''

def bwt(symbol, ):
    symbol = p[k]
    low = cfunc(symbol) + 1
    high = cfunc(symbol + 1)
    i = k - 1
    while low<=high and i>= 1:
        symbol = p[i]
        low = lfc(low - 1, symbol) + 1
        high = lfc(lfc(high, symbol))
        i -= 1
    return low, high

p = input('enter substring:')
k = len(p)