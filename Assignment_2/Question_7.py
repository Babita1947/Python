# Q_7. Write a python script to count digits in a given number.

n = int(input("Enter a number : "))
count = 0
while n!=0:
    n = n//10
    count += 1
print("Digits = ",count)