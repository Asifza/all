def increment(n):
    i = 0
    while i> -4:
        if  n[i-1]>=9:
            n[i-1]=0
            n[i-2]+=1
        i+=1
n = [2, 3, 9, 9]
increment(n)
print(n)