h= ["Asif", "Shadab", "Saif","shoeb","panther", "adnan"]
n=int(len(h))
a = h[0]
b = h[-1]
h.pop(0)
h.pop(-1)
h.insert(0, b)
h.insert(n, a)
print(h)