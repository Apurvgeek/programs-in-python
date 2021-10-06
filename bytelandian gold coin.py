from functools import lru_cache


@lru_cache(maxsize=None)
def check(num):
  if num<12:
   return num
  else:
    return check(int(num/4))+check(int(num/2))+check(int(num/3))



for each in range(10):
  x = int(input())
  y = check(x)
  print(y)
