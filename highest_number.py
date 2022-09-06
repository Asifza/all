def maximum(n1, n2, n3):
    if (n1>n2):
        if (n1>n3):
            return n1
        else:
            return n3
    else:
        if (n2>n3):
            return n2
        else:
            return n3
n1 = int(input("Enter no 1: "))
n2 = int(input("Enter no 2: "))
n3 = int(input("Enter no 3: "))
m = maximum(n1, n2, n3)
print("The greatest no is ", m)