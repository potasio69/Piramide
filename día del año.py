def año():
    a = input("Indica el día: ")
    b = input("Indica el número del mes: ")
    c = input("Indica el año: ")
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
        return año()
    b= str(b)
    a= str(a)
    c=str (c)
    print (a + " de " + b + " del " + c)
año()
