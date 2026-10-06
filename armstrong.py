n = int(input("Enter number to check: "))
temp = n
sum_ = 0
x = len(str(n))
while(temp>0):
    i = temp%10
    sum_ += i**x
    temp = temp//10
if(sum_==n):
    print("It is an Armstrong Number")
else:
    print("Not an Armstrong Number")
