# Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.

x = complex(input("Enter a number : "))

if x.real > x.imag :
    print("Real part is greater ",x.real)
elif x.real < x.imag :
    print("Imaginary part is greater ",x.imag)
else :
    print("Both are equal")

