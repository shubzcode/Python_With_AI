# 7. Write a program to find out whether a given post is talking about “Harry” or not 

post = input("Enter the post: ")

if("Shubham".lower() in post.lower()):
    print("This post is talking about Shubham")
else:
    print("This post is not talking about Shubham")