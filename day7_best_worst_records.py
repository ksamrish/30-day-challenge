inp = int(input())
l = list(map(int,input().split(' ')))

count1 = 0
count2 = 0
max= l[0]
min = l[0]

for i in range(inp):
    if(l[i]>max):
        count1+=1
        max = l[i]
    if(l[i]<min):
        count2+=1
        min = l[i]

print(count1,count2)
