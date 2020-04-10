inp = int(input())
l = list(map(int,input().split()))
d,m = map(int,input().split())
count = 0
for i in range(inp-m+1):
    sum = 0
    for j in range(i,m+i):
        sum+=l[j]
    if(sum==d):
        count+=1
print(count)
