# Q_3. Write a python script to print first 10 odd natural numbers in revers order

n = int(input("Enter a number"))
count = 0
num = 19

while count < n:
    print(num,end=" ")
    num -= 2
    count += 1