inp = list(input())
l = []
for i in range(len(inp)):
    if(l.count(inp[i])<1):
        l.append(inp[i])
print(*l,sep='')



//another method::
inp = input()
l = []
l.append(inp[0])
for i in range(len(inp)):
    for j in range(i):
        if(inp[i]==inp[j]):
            break
        if(j==i-1):
            l.append(inp[i])

print(*l,sep='')
