def ispalindrome(s):
    return s ==s[::-1]


s =str(input("enter a number "))
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("NO")
