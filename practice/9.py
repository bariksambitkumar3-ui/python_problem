# Write a Python program to count how many digits are present in a given number.
n=int(input("enter a number to count it's digits:"))
count=0
while n>0:
    digit=n%10
    n//=10
    count+=1
print(count)