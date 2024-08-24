"""
9. Write a program to print the following star pattern.
* * *
*   * for n = 3
* * * 

"""
# n = int(input("Enter the number: "))
# for i in range(n):
#     if i == 0 or i== n-1:
#         print("* "* n)
#     else:
#         print("*"+" "* (2 * n - 3)+"*")

n = int(input("Enter the number: "))
for i in range (1, n+1):
    if(i==1 or i==n):
        print("*", end="")
        print(" "* (n-2), end="")
        print(" ")