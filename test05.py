n = int (input('n = '))

for i in range(n - 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n):
    for j in range(n - i):
        print('*', end='')
    print()

""""""
n = int (input('n = '))
nt = n// 2 + 1
nb = n - nt

for i in range( nt ):
    for j in range( nt - i ):
        print('*', end='')
    for k in range( i * 2 + 1):
        print()
for i in range( nb, 0, -1 ):
    for j in range( nb - i + 1 ):
        print('*', end='')
    for k in range( i * 2 - 1):
        print()
"""
n = 5, nt = 3, nb = 2
n=5    i   j   k 
""" 