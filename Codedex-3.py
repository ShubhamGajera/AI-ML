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

# 32. Stonks

# Write code below 💖

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
# print(len(stock_prices))

# for i in range(0,20):
#   print( i , stock_prices[i])

def price_at(x):
  print(stock_prices[x-1])

def max_price(a,b):
  max_list=[]
  for i in range(a-1,b):
    max_list.append(stock_prices[i])
  print(max(max_list))

def min_price(a,b):
  min_list=[]
  for i in range(a-1,b):
    min_list.append(stock_prices[i])
  print(min(min_list))

price_at(11)
max_price(1,5)
min_price(1, 5)

# 33. Drive-Thru
# Write code below 💖

def get_item(x):
  if(x==1):
    print('🍔 Cheeseburger')
  elif(x==2):
    print('🍟 Fries')
  elif(x==3):
    print('🥤 Soda')
  elif(x==4):
    print('🍦 Ice Cream')
  elif(x==5):
    print('🍪 Cookie')
  else:
    print("Enter Ranfe from 1 to 5")

get_item(4)

# codedex
# Drive-Thru 🚙
# Codédex

def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))