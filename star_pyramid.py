for i in range(1,6):
    for j in range(1,5):
        if i<=j:
            print(" ",end="")
    for k in range(1,(i)):
       print("* ",end="")
    print()
# alternate
for i in range(0,10):
        print(" "*(11-i),"* "*i)
