n=int(input("enter a number"))
sum=1
while n>0:
    digit=n%10
    sum+=digit
    n//=10

print("sum",sum)