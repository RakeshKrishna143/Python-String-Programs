if __name__ =="__main__":
    a="GeeksforGeeks"
    a=a.lower()
    b=set(a)
    print(b)
    c="aeiou"
    d=set(c)
    e=b&d
    print(e)
    count=0
    for i in e:
        count+=a.count(i)
    print(count)
