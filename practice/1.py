# Write a program to print the sum of all digits of a number.
n=int(input("enter a number to add their digits:"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
print("sum is =",sum)