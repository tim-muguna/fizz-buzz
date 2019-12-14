number=int(input("enter number:"))
i=1
while i<=number:
    if i%5==0:
        print i,':fizz'
    else:
        print i,':buzz'
    i+=1
