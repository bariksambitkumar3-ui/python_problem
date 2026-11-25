# Write a Python program to find the GCD of two numbers.
a=int(input("enter A:"))
b=int(input("enter B:"))
temp=b
while temp!=0:
    remainder=a%temp
    a=temp
    temp=remainder
print("gcd of ",a,"and",b,"is:",a)
