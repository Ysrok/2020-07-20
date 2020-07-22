import sys

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(sys.argv[1])

print(fib(n))


"""
n = int(input("input the number: ")
l_pivo = [0, 1]
print(l_pivo)

def pivo(n):
    if n=1 and n=2:
        print("input bigger number: ")
        continue
    elif n>2:
        l_pivo.append(l_pivo[0]+l_pivo[1])
        print(l_pivo)
    return l_pivo

final=pivo(n)
print(final)
"""
