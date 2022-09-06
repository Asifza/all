inp = str(input("Enter the word: "))
old = inp
new = inp[::-1]
if old == new :
    print("this word is a palindrome")
else:
    print("This word is not a palindrome")

inp= inp.capitalize()
print(inp)

list1 = list(inp)
print(list1)

def sortString(old):
    return ' '.join(sorted(old))
print(sortString(old))