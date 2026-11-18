n=int(input("enter a number to check whether it's prime or not: "))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")