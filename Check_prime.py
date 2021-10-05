def check(n):
    i=2
    while(i*i<=n):
        if(n%i==0):
            return(False)
        i+=1
    return(True)
n=int(input())
if(check(n)):
    print("Prime Number")
else:
    print("Not a Prime Number")