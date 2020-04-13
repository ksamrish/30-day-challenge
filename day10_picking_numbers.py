inp = int(input())
arr = list(map(int,input().split()))
l = []
for i in range(inp):
    great = 0
    less = 0
    for j in range(inp):
        if(arr[i]-arr[j]==1 or arr[i]-arr[j]==0):
            great+=1
        if(arr[i]-arr[j]==-1):
            less+=1
    if(great>=less):
        l.append(great)
    elif(great<less):
        l.append(less)

print(max(l))
