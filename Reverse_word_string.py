if __name__ == "__main__": 
    strinp = input("enter the string: ")
    print(strinp)
    a=strinp.split()
    print(a)
    b=' '.join(reversed(a))
    print(b)
    
