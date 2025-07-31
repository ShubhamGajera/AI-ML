# 17. Enter PIN

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')


# 18. Guess Number
# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries<5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')



# 19. Detention 

for i in range(101):
  print(i , "I will not use Snapchat in class")


# 20. 99 Bottles
# Write code below 💖

# String concatenation

for i in range(99,0,-1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')

# 21. Fizz Buzz
# Write code below 💖

for i in range(1,101):
  if(i%3==0 and i%5==0):
    print('FizzBuzz')
  elif(i%3==0):
    print('Fizz')
  elif(i%5==0):
    print('Buzz')
  else:
    print(i)


# coddex program
# # Fizz Buzz 🐝
# # Codédex

# for num in range(1, 101):
#   if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
#   elif num % 3 == 0:
#     print('Fizz')
#   elif num % 5 == 0:
#     print('Buzz')
#   else:
#     print(num)


# 22. Grocery List

# Write code below 💖

grocery = ['🥚 Eggs','🥑 Avocados','🍪 Cookies','🌶 Hot Pepper Jam','🫐 Blueberries','🥦 Broccoli']
print(grocery)

# 23. To-Do List

# Write code below 💖

todo = ['🏦 Get quarters.',
'🧺 Do laundry.',
'🌳 Take a walk.',
'💈 Get a haircut.',
'🍵 Make some tea.',
'💻 Complete Lists chapter.',
'💖 Call mom.',
'📺 Watch My Hero Academia.']

print(todo[0])
print(todo[1])
print(todo[2:5])
print(todo[9])

# 24. Inventory
# Built-in Functions
# Python comes with some built-in functions, including ones specifically for lists.

# Here are some examples:

# The len() function returns the total length of a list.
# The max() function returns the maximum value in a list.
# The min() function returns the minimum value in a list.
# Suppose we have two lists that look like:

# stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
# stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

# print(len(stock1_prices))      # Output: 7
# print(max(stock1_prices))      # Output: 2.52
# print(min(stock2_prices))      # Output: 8.11

# We can find a list's length, minimum, and maximum within a split second, even if the list has 1000+ items!

# To learn more, here are all the Python built-in functions. However, not all built-in functions are designed to work with lists!


# Write code below 💖

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

print(max(lego_parts))
print(min(lego_parts))

# 25. Reading List

# Write code below 💖

books = ['Harry Potter',
'1984',
'The Fault in Our Stars',
'The Mom Test',
'Life in Code']

print(books)
books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)
print(books)


# 26. Mixtape

# Write code below 💖

# 💿 Theme: Indie Travel Songs

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]

for i in playlist:
  print(i)

# 27. Bucket List

# Write code below 💖

things_to_do = [
  '🚀 Create the dopest learn to code platform ever.',
  '⛰️ Hike the Pacific Crest Trail.',
  '🏡 Build an A-frame house and raise some goats.',
  '🌏 Live somewhere in Asia for a year.',
  '🎸 Release an album.',
  '📝 Write a book.',
  '🏆 Reach 100k subscribers on YouTube.',
  '🚐 Road trip with the fam.',
  '🍳 Open a cozy diner upstate.',
  '👴🏻 Grow old with no regrets.'
]

for i in things_to_do:
  print(i)


# Recap of old Chepter

# Lists are used to store different items in a single variable.
# An index is an item's position in a list. Python lists are 0-indexed.
# Slicing can access certain parts of a list with name[start:end].
# Python has built-in functions like len(), max(), min().
# Lists have built-in methods like .append(), .insert(), .remove(), .pop().
# We can iterate over a list using for-in.

#    28. D.R.Y.

# D.R.Y. 🧩
# Codédex

import random

list_of_foods = ['celery', 'broccoli', 'cabbage']

# This was the first function introduced in the course
print('Hello, World!')

# This function calculates the maximum of two numbers a and b
print(max(3, 5))

# This function calculates the minimum of two numbers a and b
print(min(-1, 7))

# This function calculates the length of a list
print(len(list_of_foods))

# This function calculates a to the power b
print(pow(2, 6))