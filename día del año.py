def a�o():
    a = input("Indica el d�a: ")
    b = input("Indica el n�mero del mes: ")
    c = input("Indica el a�o: ")
    if b==1 :
        b="enero"
    if b==2 :
        b="febrero"
    if b==3 :
        b="marzo"
    if b==4 :
        b="abril"
    if b==5 :
        b="mayo"
    if b==6 :
        b="junio"
    if b==7 :
        b="julio"
    if b==8 :
        b="agosto"
    if b==9 :
        b="septiembre"
    if b==10  :
        b="octubre"
    if b==11 :
        b="noviembre"
    if b==12 :
        b="diciembre"
    else :
        print("\nEsto wea no funciona loko")
        return a�o()
    b= str(b)
    a= str(a)
    c=str (c)
    print (a + " de " + b + " del " + c)
a�o()
