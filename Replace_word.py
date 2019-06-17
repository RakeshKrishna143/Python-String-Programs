def replaceword(strinp,ww,cw):
    a=strinp.split()
    for i in range(len(a)):
        if a[i]==ww:
            a[i]=cw
    b=' '.join(a)
    return b
if __name__ == "__main__": 
    strinp = input("enter the string: ")
    print(strinp)
    ww= input("enter the wrg word to be replaced: ")
    cw=input("enter the crt word: ")
    print(replaceword(strinp,ww,cw))
    
        
