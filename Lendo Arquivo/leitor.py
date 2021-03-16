f = open("texto", "r")
flag = False
myString = """"""

for line in f.readlines():
    for palavra in line.split():
        if palavra == '--' or palavra == '/*':
            flag = True
            elemento = palavra

        if not flag:
            myString += palavra + ' '
        else:
            if elemento == '/*' and palavra == '*/':
                flag = False
                continue
            elif elemento == '--':
                flag = False
                break

print(myString)

