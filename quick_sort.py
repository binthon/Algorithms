tab = [8,2,1,9,5]
print(tab)

def podziel(tab, start, koniec):
    strzalka = tab[koniec]
    low = start
    high = koniec - 1

    while True:
        while low <= high and tab[low] <= strzalka:
            low += 1

        while low <=high and tab[high] >= strzalka:
            high -= 1

        if low <= high:
            tab[low], tab[high] = tab[high], tab[low]
        else:
            break
    tab[koniec], tab[low] = tab[low], tab[koniec]
    return low
def quickSort(tab, start, koniec):
    if start < koniec:
        strzalka = podziel(tab, start, koniec)
        quickSort(tab, start, strzalka - 1)
        quickSort(tab, strzalka + 1, koniec)
        print(tab)

quickSort(tab, 0, len(tab) - 1)
print(tab)