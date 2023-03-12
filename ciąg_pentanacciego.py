def printpentaRec(n):
    if (n == 0 or n == 1 or
            n == 2 or n == 3 or n == 4):
        return 0
    elif (n == 5):
        return 1
    else:
        return (printpentaRec(n - 1) + printpentaRec(n - 2) + printpentaRec(n - 3) + printpentaRec(n - 4) + printpentaRec(n - 5))


def printPenta(n):
    print(printpentaRec(n))

n = 7
printPenta(n)