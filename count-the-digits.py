n=int(input("enter a number to count it's digits:"))
count=0
while n>0:
    n=n//10
    count+=1
print("count is ",count)
