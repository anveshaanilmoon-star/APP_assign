import time
def f(n):
    if n<=1:
      return n
    return f(n-1) + f(n-2)
start1=time.time()
print(f(35))
end1=time.time()
t2=end1-start1
print(t2,"seconds")

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n<=1:
      return n
    return fib(n-1) + fib(n-2)
start=time.time()
print(fib(35))
end=time.time()
t1=end-start
print(t1,"seconds")