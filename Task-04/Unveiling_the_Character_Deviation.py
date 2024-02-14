t=int(input())
for i in range(t):
    s=input()
    a="amfoss"
    
    if s==a:
        print(0)
    else:
        count=0
        for i,j in zip(a,s):
            if i!=j:
                count+=1
        print(count)
