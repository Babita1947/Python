# Write a python script to check whether a given year is a leap year or not.
x = int(input("Enter year : "))

if x%400 == 0:
    print("Leap Year")
elif x%4 == 0 and x%100 != 0 :
    print("Leap Year")
else :
    print("Non Leap Year")
