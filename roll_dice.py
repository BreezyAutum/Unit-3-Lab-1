# receives the number of dice being rolled as a parameter and returns a list of that many elements holding random integers between 1 and 6 inclusive
import random
def roll_dice():
  dlist = []
  NUM_DICE_TO_ROLL = int(input("How many dice?\n"))
  for i in range(NUM_DICE_TO_ROLL):
    roll = random.randint(1,6)
    dlist.append(roll)
  print(dlist)
  return dlist, NUM_DICE_TO_ROLL
roll_dice()