a=5
b=7
c=(7,8)[a-b>a/2]
if c-a>b+2:
    a=c+2
    print (c if a-b<10 else a-10)
else:
    b=c-5
    print((c+b-a)%5)
