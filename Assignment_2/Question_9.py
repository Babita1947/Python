# Q_9. Write a python script to check whether a given number is Prime or not.

n = int(input("Enter a number: "))

i = 2
while i<n:
    if(n%i == 0):
      break
    i += 1
if i == n:
   print("Prime")
else:
   print("Non-Prime")