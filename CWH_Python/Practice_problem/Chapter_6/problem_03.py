"""A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams."""
i = input("enter the text")
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
if(p1 in i or p2 in i or p3 in i or p4 in i):
    print("Spam")
else:
    print("not Spam")