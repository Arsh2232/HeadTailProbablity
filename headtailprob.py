import random

# Global variables
options = ['heads', 'tails']
headCounter = 0
TailCounter = 0

def coinFlip(trials):
    global headCounter, TailCounter
    for _ in range(trials):
        flip = random.choice(options)
        if flip == 'heads':
            headCounter += 1
        elif flip == 'tails':
            TailCounter += 1

def runTrials(trials):
    coinFlip(trials)
    headProbability = (headCounter / trials) * 100
    tailsProbability = (TailCounter / trials) * 100
    
    print("Probability of getting heads in {} trials = {:.2f}%".format(trials, headProbability))
    print("Probability of getting tails in {} trials = {:.2f}%".format(trials, tailsProbability))

# Run the trial
runTrials(100)
