def find_place(n,b):
    mini=min(b)
    cnt=b.count(mini)
    if cnt>1:
        return "Still Aetheria"
    else:
        res=b.index(mini)+1
        return res

n=int(input())
l=list(map(int,input().split()))
print(find_place(n,l))
