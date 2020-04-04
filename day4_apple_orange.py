s,t = map(int,input().split(' '))
a,o = map(int,input().split(' '))
m,n = map(int,input().split(' '))
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
count1 = 0
count2 = 0
for i in range(m):
    add = a + l1[i]
    if(add>=s and add<=t):
        count1+=1
for i in range(n):
    add = o + l2[i]
    if(add>=s and add<=t):
        count2+=1

print(count1)
print(count2)
