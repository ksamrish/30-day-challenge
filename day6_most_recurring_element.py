l = []
inp = input()
count = [1]*len(inp)
for i in range(len(inp)):
    count[i]=1
for i in range(len(inp)):
    for j in range(i+1,len(inp)):
        if(inp[i]==inp[j]):
            count[i]+=1
for i in range(len(inp)):
    if(count[i]==max(count)):
        l.append(inp[i])
print(*set(l))
