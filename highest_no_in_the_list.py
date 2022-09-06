a = [""]
x = 3
a.pop(0)
z = int(len(a))
while z<=x:
    y = input("Enter a number: \n")
    a.append(y)
    z=z+1
a.sort()
print("The highest number in the list is:", a[-1])