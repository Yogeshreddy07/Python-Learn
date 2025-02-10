"""Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50   => F """
i=int(input("enter the marks:"))

if (i<=100 and i>90):
    print("Your grade is: Ex")
elif (i<=90 and i>80):
    print("Your grade is: A")
elif (i<=80 and i>70):
    print("Your grade is: B")
elif (i<=70 and i>60):
    print("Your grade is: C")
elif (i<=60 and i>50):
    print("Your grade is: D")
elif (i<50):
    print("Your grade is: F") 

