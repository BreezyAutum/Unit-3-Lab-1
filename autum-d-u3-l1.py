import random 
NUM_DICE_TO_ROLL = 5 
SEED = 2183

# implement roll_dice() here! 
def roll_dice():
  '''Rolls dice and sets them to a list, so the full list can be displayed.'''
  global dlist; dlist = []
  NUM_DICE_TO_ROLL = int(input("How many dice?\n"))
  for i in range(NUM_DICE_TO_ROLL):
    roll = random.randint(1,6)
    dlist.append(roll)
  print(dlist)
  return dlist, NUM_DICE_TO_ROLL, roll
roll_dice()

# implement most_repeats() here! 
def repeats():
    '''Finds how many times the most common number was rolled in roll_dice'''
    repeats = roll_dice.dlist.count
    repeats = int(repeats)
    return repeats
 
def main():
    random.seed(SEED) 
    # implement remaining logic here! 
    print("Your roll of", dlist, "contains", repeats," of a kind.")
    again = input("Do you want to roll again?\n")
    if "Y" in again:
        roll_dice()
    elif "N" in again:
        exit()
    else:
        print("ERROR: User didn't eneter Y or N")
        exit()
if __name__ == "__main__": 
    main()
