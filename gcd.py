a=int(input("enter A:"))
b=int(input("enter B:"))
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("gcd of A and b is:",gcd)