Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
a=input("Primer numero= ")
b=input("Segundo numero= ")
c=raw_input("Escribe S si quieres sumar, R resta, M multiplicacion o D para una division: ")

if c is "S":
    print a+b
if c is "R":
    print a-b
if c is "M":
    print a*b
if c is "D":
    print a/b
