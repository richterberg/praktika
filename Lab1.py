def test(string, i=0):
    if i == len(string):   	 
        print("".join(string))
    for j in range(i, len(string)):
        slova = [c for c in string]
        slova[i], slova[j] = slova[j], slova[i]
        test(slova, i + 1)
print(test('lab1'))
