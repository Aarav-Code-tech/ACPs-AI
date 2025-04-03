import random
a = ["rock","paper","scissor"]
b = random.choice(a)
c = input("Enter rock paper or scissor : ")
d = c.lower()
print("Computers Choice :",b)
if b==d:
  print("tie")
elif b=="rock":
  if d == "paper":
    print("You win")
  else:
    print("The winner is",b)
elif b=="scissor":
  if d == "rock":
    print("You win")
  else:
    print("The winner is",b)
elif b=="paper":
  if d == "scissor":
    print("You win")
  else:
    print("The winner is",b)
else:
  print("Invalid")
