Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def es_primo(numero):
  
    for i in range(2,numero):
        if (numero%i)==0
            return False
    return True
 
while True:
    try:
        numero = int(raw_input("inserta un numero (0) salir >> "))
        if numero==0:
            break
        if es_primo(numero):
            print "\nEl numero %s es primo" % numero
        else:
            print "\nEl numero %s NO es primo" % numero
    except:
        print "\nEl numero tiene que ser entero"
