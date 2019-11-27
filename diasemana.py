Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def dias ():
    a=input("Numero del dia= ")

    if a is 1:
        print ("Lunes")
    elif a is 2:
        print ("Martes")
    elif a is 3:
        print ("Miercoles")
    elif a is 4:
        print ("Jueves")
    elif a is 5:
        print ("Viernes")
    elif a is 6:
        print ("Sabado")
    elif a is 7:
        print ("Domingo")
    elif a >= 7:
        print ("No existe")
dias()
