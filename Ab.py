from google import genai
from google.genai import types

gapi_key="AIzaSyB5UwPhatHQ8h0XqhFXx8BvxpONMprIXRo"

client=genai.Client(api_key=gapi_key)

def a(prompt, temperature=0.5):
  try:
    contents=[types.Content(role="user",parts=[types.Part.from_text(text=prompt)])]
    config=types.GenerateContentConfig(temperature=temperature)
    response=client.models.generate_content(model="gemini-2.0-flash",contents=contents,config=config)
    return response.text

  except Exception as e:
    return f"the error is {e}"
def rl():
  print("Welcome to '''reinforcement learning''' ")
  prompt=input("Quickly enter your prompt(I am not asking) : ")
  ab=a(prompt)
  print(f"Your initial answer is {ab}")
  rating=5
  print("Thank you for rating us 5 out of 5")
  feedback=input("Feedback : ")
  print("The feedback you have give is- This is a very good AI chatbot and I would like to visit it again.")
  abc=a(feedback)
  print(f"Your final answer is {abc}")
def role():
  print("Welcome to role based learning")
  x=input("Enter Category : ")
  y=input("Enter the topic : ")
  z=input("Enter the type 1.Teacher 2.Expert : ")
  if z=="1":
    teacher=a(y)
    print(f"Your answer is {teacher}")
  elif z=="2":
    expert=a(y)
    print(f"Your answer is {expert}")
def main():
  print("Press 1 for reinforcement learning and 2 for role-based learning")
  q=int(input())
  if q==1:
    rl()
  elif q==2:
    role()
  else:
    print("Invalid input")
main()
