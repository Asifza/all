z = input("Enter your username: ")
x = int(len(z))
if x<10:
    print("your username is too small")
elif x>10:
    print("your username is too large")
else:
    print("your username has 10 characters")