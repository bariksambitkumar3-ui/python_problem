# Write a Python program that calculates the sum of all digits of a given number.
n=int(input("enter a number to reverse :"))
rev=0

while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10

print("after reverse:",rev)