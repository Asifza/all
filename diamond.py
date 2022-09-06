n=int(input("Enter the number of rows: "))
m=n-2
for i in range (n):
    print(" " * (n-i-1),"*" * (2*i+1)," " * (n-i-1))
for j in range (m,-1,-1):
    print(" " * (n-j-1),"*" * (2*j+1)," " * (n-j-1))