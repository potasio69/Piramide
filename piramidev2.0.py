def piramide():
    rango= int(input("Número de flas: \n"))
    for i in range(1, rango+1):
        print"/"*(rango-(i-1))+" "*((i)*2-1)+"""'\'"""*(rango-(i-1))
piramide()
