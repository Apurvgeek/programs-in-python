from functools import reduce
numlst=list(map(int,input().split(" ")))
num=reduce(lambda x,y:x+y,numlst)
print(num)
