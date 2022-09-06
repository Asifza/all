def table(n, i):
    while i < 11:
        print("f.{n} X {i} = {n*i}")
        i=i+1
n = int(input('Enter the number: '))
i= 1
z = table(n, i)
print(z)