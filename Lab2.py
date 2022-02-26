from itertools import zip_longest, cycle
 
 
def test(data: str, key: str):
    xored = ''
    for (x, y) in zip_longest(data, cycle(key)):
        if not x:
            break
        xored += chr(ord(x) ^ ord(y))
    return xored
 
 
a = test('Лаба3', '123')
print(a)
print(test(a, '123'))
