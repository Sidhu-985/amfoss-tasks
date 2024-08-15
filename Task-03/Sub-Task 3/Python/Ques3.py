n = 5  

for i in range(1, n + 1, 2): 
    for j in range((n - i) // 2):
        print(' ', end='')
    
    for k in range(i):
        print('*', end='')

    print()


for i in range(n - 2, 0, -2):  
    for j in range((n - i) // 2):
        print(' ', end='')

    for k in range(i):
        print('*', end='')
    
    print()
