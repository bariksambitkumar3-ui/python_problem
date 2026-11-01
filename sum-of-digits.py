n=int(input("enter a number to sum their digits:"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print("sum of the digits of the number is",sum)