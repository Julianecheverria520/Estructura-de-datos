Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(10))
SyntaxError: invalid syntax
>>> 
