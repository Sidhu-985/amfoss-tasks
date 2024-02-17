n = int(input())
for _ in range(n):
    num = int(input())
    
    a = []  
    b = []
    for i in range(2, num+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            a.append(i)
    print(a)
    for k in a :
        if num % k == 0 :
            b.append(k)
    print(max(b))
    
