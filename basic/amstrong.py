n=int(input("enter a number to check whether it is amstrong or not:"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if n==sum:
    print("amstrong number.")
else:
    print("not amstrong.")