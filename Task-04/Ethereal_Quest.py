X=[]
Y=[]
Z=[]
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    
    X.append(x)
    Y.append(y)
    Z.append(z)
    sx=sum(X)
    sy=sum(Y) 
    sz=sum(Z)
if sx==sy==sz==0:
    print("YES")
else:
    print("NO")
