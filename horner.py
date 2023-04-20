a = int(input("Podaj miejsce zerowe: "))
tablica = []
d=[]
wynik=[]
stopien_wiel = int(input("Podaj stopień wielomianu: "))
for x in range(stopien_wiel+1):
    c= ("x"+str((stopien_wiel)-x))
    if (c=="x1"):
        c="x"
    elif(c=="x0"):
        c="C"
    d.insert(stopien_wiel,int(input("Podaj współczynnik: " +c+" ")))

for x in range(len(d)):
    if(x==0):
        wynik.insert(x,d[x])
    else:
        wynik.insert(x,((a*wynik[x-1])+d[x]))

if(wynik[-1]==0):
    wynik.pop(-1)
s=("Wynik:{}").format(wynik)
print(s)


f=[]
