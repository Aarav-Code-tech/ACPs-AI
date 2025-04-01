from textblob import TextBlob
name = input("What's your name? ")
feeling = input(f"Hi {name}, how are you feeling today? ")
blob = TextBlob(feeling)
polarity = blob.sentiment.polarity
if polarity > 0:
    print("Nice to hear that!")
elif polarity < 0:
    print("I hope things get better soon.")
else:
    print("Thanks for sharing. Hope you have a good day!")