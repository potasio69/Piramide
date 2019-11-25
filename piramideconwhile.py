filas = int(input("Numero de filas :"))
i=" "
x="*"
t=1
p=34
while filas != 0 :
    if t == 1 :
        print(p*i+x*t)
        t+=2
        
    else:
        p-=1
        print(p*i+x*t)
        t+=2
    filas-=1     
