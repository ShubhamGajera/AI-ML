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