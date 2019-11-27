Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def ecuacion():

    print("***************************")
    print("*Calculadora de polinomios*")
    print("***************************")
    print("")
    print("Ax^2 + Bx + C = 0")
    
    num1 = input("A: ")
    num2 = input("B: ")
    num3 = input("C: ")

    sum = num2**2 - 4*num1*num3

    if(sum >= 0):
        
        result1 = (-num2 + math.sqrt(num2**2 - 4*num1*num3)) / 2*num1
        result2 = (-num2 - math.sqrt(num2**2 - 4*num1*num3)) / 2*num1

        rst1=str(result1)
        rst2=str(result2)

        print("La respuestas son " + rst1 +" y " + rst2 + ".")
    else:
        print("No se puede")
    
ecuacion()
