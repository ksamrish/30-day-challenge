x1,v1,x2,v2 = map(int,input().split(' '))
# start1 = x1
# start2 = x2
if((x1>x2 and v1>v2) or (x2>x1 and v2>v1)):
    print("NO")
elif(x1==x2 and v1==v2):
    print("YES")
else:
    for i in range(9999):
        x1+=v1
        x2+=v2
        if(x1==x2):
            print("YES")
            break
    else:
        print("NO")
