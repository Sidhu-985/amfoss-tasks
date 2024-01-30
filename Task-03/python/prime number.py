n=int(input("Enter the number:"))

if n<=1:
    print(n,"is not a prime number")
else:
    for i in range(2,n+1):
        flag=0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                flag=1
        
        if flag==0:
            print(i,"is a prime number")
