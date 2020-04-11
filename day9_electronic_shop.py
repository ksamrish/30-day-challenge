max,a,b = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
temp = 0
for i in range(len(l1)):
    for j in range(len(l2)):
        sum=0
        sum+=l1[i]+l2[j]
        if(sum>temp and sum<=max):
            temp = sum
if(temp==0):
    print("-1")
elif(temp<=max):
    print(temp)
else:
    print("-1")
