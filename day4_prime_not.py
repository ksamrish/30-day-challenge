inp = int(input("Enter number to find prime or not: "))
if(inp==1):
        print("neither prime nor composite")

for i in range(2,int((inp/2))+1):
    if(inp%i==0):
        print("not prime")
        break
else:
    if(inp!=1):
        print("prime")
