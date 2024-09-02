with open("input.txt", "r") as file:
    n = int(file.read().strip())

with open("output.txt", "w") as file:
    for i in range(1, n + 1, 2):
        for j in range((n - i) // 2):
            file.write(' ')
        
        for k in range(i):
            file.write('*')
        
        file.write('\n')

    for i in range(n - 2, 0, -2):
        for j in range((n - i) // 2):
            file.write(' ')
        
        for k in range(i):
            file.write('*')
        
        file.write('\n')
