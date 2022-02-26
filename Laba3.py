A = 15
B = 17
M = 4096
Y0 = 4003
 
 
def Gamma(y):
    gamma_list = []
    for _ in range(8):
        y = (A * y + B) % M
        gamma_list.append(y)
    return gamma_list
 
 
def Crypt():
    gamma = Gamma(Y0)
    res = open("Result.txt", "w",encoding="utf-8")
    with open('Sourse.txt', 'r',encoding="utf-8") as f:
        r_int = ""
        r=""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " "+str(ord(item) ^ gamma[i])
                    r = r +" "+chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
 
            else:
                break
    print(r_int)
    res.close()
 
Crypt()
 
def DeCrypt():
    gamma = Gamma(Y0)
    res = open("NewResult.txt", "w",encoding="utf-8")
    with open('Result.txt', 'r',encoding="utf-8") as f:
        r_int = ""
        r = ""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " " + str(ord(item) ^ gamma[i])
                    r = r + chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
            else:
                break
    print(r_int)
    res.close()
 
DeCrypt()