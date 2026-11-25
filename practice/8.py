# Write a Python program to find LCM.
a=int(input("enter A:"))
b=int(input("enter B:"))
temp=b
t=a
while temp!=0:
    remainder=t%temp
    t=temp
    temp=remainder
lcm=(a*b)//t
print("lcm of ",a,"and",b,"is:",lcm)
print("Git Hub Check")