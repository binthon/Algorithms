tab = [8,2,1,9,5]
print(tab)

i = 1
while i < len(tab):
    klucz = tab[i]
    j = i - 1
    while j >= 0 and klucz < tab[j]:
        tab[j + 1] = tab[j]
        j -= 1
    tab[j + 1] = klucz
    i +=1
print(tab)