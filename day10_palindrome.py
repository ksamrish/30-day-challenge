inp = input()
i = 0
n = len(inp)
while(i<int(n/2)):
    if(inp[i]!=inp[n-i-1]):
        print("NO")
        break
    if(i==int(n/2)-1):
        print("YES")
    i+=1
