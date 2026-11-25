# Write a Python program to find the largest digit in a given number.
n=int(input("enter a number:"))
largest=0

while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n//=10
    
print(largest)  
