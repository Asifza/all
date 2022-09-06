from ast import Break


def add(n):
    if n<0:
        print("invalid statement")
        
    else:
        if n ==1:
            return n
        elif n==0:
            return n
        else:
            return n+add(n-1)
n = int(input("Enter the number you want to find the addition of: "))
f = add(n)
print(f)