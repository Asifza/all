n= 2
i= 1
for j in range(-1, n):
    if i == 0 and j == 0:
        print("* *")
        i=i-1
        j=j+1
    elif i <0:
        print("*"*(2*j+1))
        i=i-1
        j=j+1
    else:
        print("*"*(2*i+1), "*"*(2*j+1))
        i=i-1
        j=j+1