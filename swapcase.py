a="hellO"
b=''
for i in a:
    if ord(i)>=97:
        b+=chr(ord(i)-32)
    else:
        b+=chr(ord(i)+32)
print(b)
print(b.swapcase())       
