# Q_1. Write a python script to print first 10 odd natural numbers.
n=int(input("Enter a number : "))
count = 0
num = 1
while count < n:
    print(num,end=" ")
    num += 2
    count += 1