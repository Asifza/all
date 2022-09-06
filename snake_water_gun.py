import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "g":
            return True
        elif you == "w":
            return False
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False
    elif comp == "W":
        if you == "s":
            return True
        elif you == "g":
            return False
print("Comp Turn: Snake(s) Water(w) or Gun(g)")
randno = random.randint(1,3)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno ==3:
    comp = "g"

you = input("Your Turn: Snake(s) Water(w) or Gun(g): ")
a = gameWin(comp,you)
print(f"computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie")
elif a:
    print("You win")
else:
    print("you lose")