import random 
NUM_DICE_TO_ROLL = 5 
SEED = 2183

# implement roll_dice() here! 
import roll_dice

# implement most_repeats() here! 
def most_repeats(repeats):
    """receives a list of integers (representing dice values) as the parameter and returns the highest number of repeated values. E.g. if the received list contains [1, 1, 4, 4, 4], the returned value would be 3"""
    repeats = roll_dice.dlist.count()
    return repeats
 
def main(): 
    random.seed(SEED) 
    # implement remaining logic here! 
    print(f"Your roll of {roll_dice(dlist)} contains {most_repeats(repeats)} of a kind.\nDo you want to roll again (Y/N)?")
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
