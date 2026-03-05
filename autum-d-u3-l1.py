import random 
NUM_DICE_TO_ROLL = 5 
SEED = 2183

# implement roll_dice() here! 
import roll_dice

# implement most_repeats() here! 
def repeats():
    global counts; counts = roll_dice.dlist.counts
    return counts
 
def main():
    random.seed(SEED) 
    # implement remaining logic here! 
    print(f"Your roll of {roll_dice.dlist} contains {repeats.counts} of a kind.")
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
