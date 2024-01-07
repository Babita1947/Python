#Q_2. Write a program to check whether a given number is positive or non positive ?

# x = int(input("Enter a number"))

# if x>0:
#     print("Positive")
# if x<=0:
#     print("Non-positive")

#Q_3. Write a program to print grade obtained in a test. Take marks obtained from user and display the grade.
#     90 < marks <= 100   A
#     80 < marks <= 90   B
#     70 < marks <= 80   C
#     60 < marks <= 70   D
#     50 < marks <= 60   E
#     below 50           F

# x=float(input("Enter your marks : "))

# if x>90 and x<=100:
#     print("Grade-A")
# elif x>80 and x<=90:
#     print("Grade-B")
# elif x>70 and x<=80:
#     print("Grade-C")
# elif x>60 and x<=70:
#     print("Grade-D")    
# elif x>=50 and x<=60:
#     print("Grade-E")
# else :
#     print("Grade-F")

# Q_3. Check whether a given number is odd or even ? using single line if else 
 
x = int(input("Enter a number : "))

print("Even") if x%2 == 0 else print("Odd")

print("Even" if x%2 == 0 else "Odd")