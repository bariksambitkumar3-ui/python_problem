# Write a Python program to find the smallest digit in a given number.
n=int(input("enter a number to find it's smallest digit:"))
smallest=10
while n>0:
    digit=n%10
    if digit<smallest:
        smallest=digit
    n//=10
print("smallest digit is :",smallest)