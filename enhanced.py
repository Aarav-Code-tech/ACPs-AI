while True:
    print("Hello, what can I call you?")
    a = input()
    b = input(f"Hello {a} i am AI. How are you feeling today(Good/Not so well)? ")
    c=b.lower()
    if c=="good":
        print("Good to hear that.")
    elif c=="not so well":
        print("Oh! I hope things get better soon.")
    else:
        print("Please enter your answer as Good or Not so well")
        continue
    print(f"Nice meeting you {a},Goodbye")
    break

