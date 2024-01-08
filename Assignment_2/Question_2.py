# Q_2. Write a python script to print first N even natural numbers.
n = int(input("Enter a number"))

num = 2

for i in range(0,n):
    print(num,end=" ")
    num += 2

