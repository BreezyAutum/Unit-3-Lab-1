import random 
NUM_DICE_TO_ROLL = 5 
SEED = 2183
import roll_dice

# implement roll_dice() here! 
roll_dice.roll_dice()
    
# implement most_repeats() here! 
def most_repeats(repeats):
    """receives a list of integers (representing dice values) as the parameter and returns the highest number of repeated values. E.g. if the received list contains [1, 1, 4, 4, 4], the returned value would be 3"""
    repeats = roll_dice.dlist.count()
    return repeats
 
def main(): 
    random.seed(SEED) 
    # implement remaining logic here! 
 
if __name__ == "__main__": 
    main()