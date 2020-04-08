inp = list(input())
l = []
for i in range(len(inp)):
    if(l.count(inp[i])<1):
        l.append(inp[i])
print(*l,sep='')
