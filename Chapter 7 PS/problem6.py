#6. Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * 1
    
print(f"The Factorial of {n} is {product}")