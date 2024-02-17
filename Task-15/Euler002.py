t=int(input())
for _ in range(t):
    N = int(input())
    a,b=0,1
    sum=0
    lst=[]
    
    while N >= a:
        lst.append(a)
        a,b=b,a+b
    
    for i in lst:
        if i%2==0:
            sum+=i
    
    print(sum)
