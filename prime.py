n = int(input("Enter a number to check : "))
for i in range(2,(n//2)+1):
    if(n%i==0):
        print("Not a Prime Number")
        break;
else:
    print("Prime Number")
