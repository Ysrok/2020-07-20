
l1 = ["A", "T", "G", "C"]
l2 = ["A", "T", "G", "C"]

import sys
def mer(l1, l2, n):
    if n == 1:
        return l2
    ltmp = []
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)
    return mer(l1, ltmp, n-1)

n = int(sys.argv[1])
print(mer(l1, l2, n))

"""
ltem=[]
for i in l1:
    for j in l2:
        ltem.append(i+j)
        print(ltem)
"""
"""
ltem=[]
def mer(l1, l2, n):
    if n==1:
        return l2
    elif n==2:
        for i in l1:
            for j in l2:
                ltem.append(i+j)
                print(ltem)
        return ltem.append(i+j)
    else:
        for a in ltem:
            for b in l2:
                ltem.append(a+b)
                print(ltem)
        return ltem.append(a+b)

final=mer(l1, l2, 3)
print(final)
"""



