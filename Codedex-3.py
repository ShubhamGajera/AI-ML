# 29. Fortune Cookie

# Write code below 💖
import random

def fortune():
  a=random.randint(0,7)
  if(a==0):
    print("Don't pursue happiness – create it.")
  elif(a==1):
    print("All things are difficult before they are easy.")
  elif(a==2):
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif(a==3):
    print("Someone in your life needs a letter from you.")
  elif(a==4):
    print("Don't just think. Act!")
  elif(a==5):
    print("Your heart will skip a beat.")
  elif(a==6):
    print("The fortune you search for is in another cookie.")
  else:
    print("Help! I'm being held prisoner in a Chinese bakery!")

fortune()

# 30. Mars Orbiter

def distance_to_miles(kilometer):
  print(kilometer/1.609)

distance_to_miles(1000)

# 31. Calculator |
# Write code below 💖

def add(a, b):
  print(a+b)

def subtract(a, b):
  print(a-b)

def multiply(a, b):
  print(a*b)

def divide(a, b):
  print(a/b)

def exp(a, b):
  print(a**b)

add(10,2)
subtract(10,2)
multiply(10,2)
divide(10,2)
exp(10,2)