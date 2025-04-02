import random
a = ["rock","paper","scissor"]
b = random.choice(a)
c = input("Enter rock paper or scissor : ")
print("Computers Choice :",b)
if b==c:
  prin   t("tie")
elif b=="rock":
  if c == "paper":
    print("The winner is",c)
  else:
    print("The winner is",b)
elif b=="scissor":
  if c == "rock":
    print("The winner is",c)
  else:
    print("The winner is",b)
elif b=="paper":
  if c == "scissor":
    print("The winner is",c)
  else:
    print("The winner is",b)
else:
  print("Invalid")
    
  
