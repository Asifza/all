m = 5
o = 0
arr =[]
while o < m:
    z=input("Enter a number: ")
    arr.append(z)
    o=o+1
#x = 0
#i =0
#large = []
#print(arr)
#while i < m:
#    if arr[x]>arr[x+1]:
#        a =arr[x]
#        x=x+1
#        i=i+1
#        large.append(a)
#    else:
#        a= arr[x+1]
#        x=x+1
#        i=i+1
#        large.append(a)
#print(large[-2])

#salman method
new = set(arr)
new1 = list(new)
new1.sort()
print(new1[-2])