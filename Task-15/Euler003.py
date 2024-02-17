t = int(input())
for i in range(t):
    N=int(input())
    list1=[N]
    list2=[]
    for i in list1:
        temp_list=[]
        for j in range(2,i+1):
            if i%j==0:
                temp_list.append(j)
                i=i//j
        list2.append(max(temp_list))
    print(max(temp_list))
