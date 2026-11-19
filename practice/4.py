# Write a Python program to check whether a number is an Armstrong number.
n=int(input("enter a number to check wheather it is amstrong or not:"))
sum=0
temp=n
l=len(str(temp))
while temp>0 and l!=0:
    digit=temp%10
    sum=sum+digit**l
    temp//=10
if n==sum:
    print("amstrong .")
else:
    print("not amstrong.")
