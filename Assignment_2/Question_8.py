# Q_8. Write a python script to calculate sum of the digits of a given  number.

n = int(input("Enter a number : "))
sum = 0
x = 0
while n!=0:
    x = n%10
    sum = sum + x
    n = n//10
print("Sum of digits = ",sum)