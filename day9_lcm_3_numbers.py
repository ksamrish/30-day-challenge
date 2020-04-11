a,b,c = map(int,input("Enter three numbers to find lcm: ").split())
max = min(a,b,c)
temp = max
while(1):
    if(temp%a==0 and temp%b==0 and temp%c==0):
        break
    temp+=1;
print(temp)

