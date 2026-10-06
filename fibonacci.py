a =0
b=1
n = int(input("Enter the number till where you want the fibonacci series"))
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
