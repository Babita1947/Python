# Q_6. Write a python script to calculate sum of first N natural numbers.

n = int(input("Enter a number : "))
sum = 0

for i in range(1,n+1):
    sum = sum + i
print("Sum = ",sum)

