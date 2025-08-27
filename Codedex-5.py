# 39. Slot Machine

# Write code below 💖

import random


def play():
  plays='Y'
  while(plays=='Y'):
    symbols = ['🍒',' 🍇', '🍉', '7️⃣']
    results = random.choices(symbols,k=3)
    print(results[0],'|',results[1],'|',results[2])
    if(results[0]==results[1]==results[2]=='7️⃣'):
      print("Jackpot! 💰")
    else:
      print('Thanks for playing!')
    plays=input('If want to play Write "Y" if not than "N" :')

play()


# codedex

# Slot Machine 🎰
# Codédex

import random

symbols = [
  '🍒',
  '🍇',
  '🍉',
  '7️⃣'
]

def play():

  for i in range(1, 51):    
    results = random.choices(symbols, k=3)
    print(f'{results[0]} | {results[1]} | {results[2]}')
    win = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

    if win:
      print('Jackpot!!! 💰')
      break
    else:
      results = random.choices(symbols, k=3)

answer = ''
while answer.upper() != 'N':
  play()
  answer = input('Keep playing? (Y/N) ')

print('Thanks for playing!')


# 40. Solar System |

# Write code below 💖

from math import pi 
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet= ch(planets)
print(random_planet)
r=1
if random_planet == 'Mercury':
  r=2440
elif random_planet == 'Venus':
  r= 6052
elif random_planet == 'Earth':
  r= 6371
elif random_planet == 'Mars':
  r= 3390
elif random_planet == 'Saturn':
  r= 58232
else:
  print('Oops! An error occurred.')
area = 4 * pi * r ** 2

print(f'Area of {random_planet} is {area}')

# 43. Zen of Python

print('21 July 2025')
print('happy.......')
print('want to become AI/ML Engineering')
print('Stay consistent and stay focuesd')
print('😎')

# The Zen of Python 📜
# Codédex

import this

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""