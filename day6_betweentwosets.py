a,b = map(int,input().split(' '))
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = []
max1 = max(l1)
max2 = max(l2)
i = max1
count3 = 0
while(i<=max2):
    count1 = 0
    count2 = 0
    for j in l1:
        if(i%j==0):
            count1=1
        else:
            count1 = 0
            break
    for j in l2:
        if(j%i==0):
            count2 = 1
        else:
            count2 = 0
            break
    if(count1==1 and count2==1):
        count3+=1
    i+=1
print(count3)
