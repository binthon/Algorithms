number1 = 0
number2 = 1
fib = []
n = 1
print("Wpisz ilość powtórzeń: ")
loop = int(input())
fib.append(number1)
fib.append(number2)

for i in range(loop):
    przeskok = fib[n]+fib[n-1]
    fib.append(przeskok)
    n += 1
print(fib)


n = 2
tabela_zloty_podzial = []
for i in range(loop):
    zloty_podzial = fib[n] / fib[n-1]
    tabela_zloty_podzial.append(zloty_podzial)
    n += 1
print(tabela_zloty_podzial)


