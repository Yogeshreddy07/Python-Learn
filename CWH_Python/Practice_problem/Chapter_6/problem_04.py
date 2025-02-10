#Write a program to find whether a given username contains less than 10 characters or not.
username=input("Enter the username:")
l=len(username)
if (l>10):
    print("given username contains more than 10 characters")
else:
    print("given username contains less than 10 characters")