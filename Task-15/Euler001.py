t=int(input())
for i in range(t):
    N=int(input())
    sum=0
    for i in range(N):
        if i%3==0 or i%5==0:
            sum+=i
    print(sum)
