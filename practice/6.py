# Write a Python program to check whether a given number is prime.(by using while loop.)
n=int(input("enter a number to check wheateher it is prime or not:"))
if n<=1:
    print("not prime.")
else:
    i=2
    is_prime=True
while n>i:
    if n%i==0:
        is_prime=False
        break
    i+=1
if is_prime:
    print("prime.")
else:
    print("not prime.")