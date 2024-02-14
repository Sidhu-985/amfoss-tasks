s=input()
a="hello"
j=0
cnt=0
for i in s:
    if j<len(a) and i==a[j]:
        j+=1
        cnt+=1
    else:
        continue
if cnt==5:
    print("YES")
else:
    print("NO")
