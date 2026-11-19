# Write a Python program to check whether a given number is prime. (by using for loop.)
n=int(input("enter a number to check wheather it is prime or not:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")
