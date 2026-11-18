original=int(input("enter a number:"))
rev=original=str(original)
rev=rev[::-1]
print(rev)
if rev==original:
    print("palindrome number")
else:
    print("not palindrome")