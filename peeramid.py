for i in range(1,6):
    for j in range(1,5):
        if i<=j:
            print(" ",end="")
    for k in range(1,(2*i)):
        if k<=i:
            print(k,end="")
        if k>i:
            print(2*i-k,end="")
    print()
# alternate
for i in range(0,10):
    print(" "*(11-i),int((1+((10)**i)+((10)**(i-1)))**2))
