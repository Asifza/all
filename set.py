import collections
a = [5, 5, 8, 3, 8, 9, 7, 6, 7]
m = [item for item, count in collections.Counter(a).items() if count > 1]
print(m)