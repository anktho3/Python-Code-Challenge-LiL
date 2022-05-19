import random

def dice_roll(*args):
    '''Return a table of probability for each possible outcome of a dice roll'''
    outcome_dict = {}
    rolled = int()
    for rolls in range(0, 1000000):
        outcome = int(0)
        for arg in args:
            roll = random.randint(1,arg)
            outcome += roll
        if outcome in outcome_dict.keys():
            newVal = outcome_dict.get(outcome) + 1
            outcome_dict.update({outcome:int(newVal)})
        else:
            outcome_dict.update({outcome:1})
        rolled += 1
    print("\n------Outcomes------\n")
    print("Outcome  Times-landed    Probability")
    for i in sorted (outcome_dict):
        probability = float(outcome_dict[i]) / 1000000
        probability = 100 * probability
        print('{:<8}'.format(i), "  ", '{:>9}'.format(outcome_dict[i]), "   ", '{:>8.2f}'.format(probability), "%")
