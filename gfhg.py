dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(id(dict1), id(dict2))
print(dict1==dict2, dict1 is dict2)