# Write a Python program to check whether a number is a palindrome.
n=int(input("enter a number to check wheather it is palindrome or not :"))
rev=0
temp=n
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if n==rev:
    print("palindrome")
else:
    print("not palindrome.")