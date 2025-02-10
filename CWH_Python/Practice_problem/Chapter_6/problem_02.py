"""Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user."""

m=int(input("Enter the marks 1:"))
m1=int(input("Enter the marks 2:"))
m2=int(input("Enter the marks 3:"))
avg=(m+m1+m2)/3
if (m>33 and m1>33 and m2>33):
    print("All sub are pass and all above 33")
    if(avg>40):
        print("All clear" ,avg)
    else:
        print("the percentage is below 40 and fail" ,avg)
else:
    print("fail")