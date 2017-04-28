# Tatum Hawkins - LIS 452 - 4 credit hour

import random

# Read in the chapter. Just one for now to practice getting the glossary and words.
# Will need to make a loop to go through all of them later on.

inchapter = open('Chapter 1 Practice.txt', 'r')
chapter = inchapter.readlines()

# Find the glossary and ignore the rest of the chapter (for now).
# Should be between the line ending with "Glossary" and the line ending with "Exercises".
# Do they all have exercises? If not, then the end of the chapter file.

for line in chapter:
    if "Glossary" in line:
        gloss_start = chapter.index(line) + 1 # Because Python starts at 0, the text file at 1
        #print(gloss_start)
    if "Exercise" in line:
        gloss_end = chapter.index(line)
        #print(gloss_end)

# Split the glossary up into words and definitions. Originally I thought dictionary (sounds
# obvious as the best tool). Now I'm realizing that we didn't actually make a dictionary for
# any of our assignments - everything could be done with lists instead - so now I'm thinking
# lists. Given what I'm doing, I'm not sure there's a major difference. Maybe with the
# right/wrong list it would be important though?? Lists are ordered though. Then there could
# be the option of random word or alphabetical order... I'm getting in way over my head here.

# Paired in a single list or separate lists with matching indices? =\
vocabs = []
words = []
defs = []

for each in range(gloss_start, gloss_end, 2):
    next_pair = (chapter[each].strip(), chapter[each+1].strip())
    vocabs.append(next_pair)
    words.append(chapter[each].strip())
    defs.append(chapter[each+1].strip())

# Find out how many vocab words are in the chapter.
num_pairs = len(vocabs)

# Select a random vocab pair for the quiz question.
pick = random.randint(0, num_pairs-1) # Again with the 0 vs 1 thing
#print(pick)
print(vocabs[pick], "\n")

# Interact with the user. Give a definition and get a response.
# Check to see if the word is correct.
# How to go through all the words using random, without repeating... How does pop work?
# Maybe make a list of the numbers and then pick a random entry and then pop it out? So,
# then random would be for the positioin in the number list rather than the vocab list.
# That way the changing positions doesn't lead to repeating vocab words...

# Playing with the quiz part. 
print("DIRECTIONS: Read the following definition, then enter the correct corresponding vocabulary word. "
      "Remember, it must be spelled corretly to receive any credit.\n")
print("Definition:", defs[pick], "\n")
response = input("\t This is the definition of what vocabulary word or phrase? ")

if response == words[pick]:
    print("Correct!")
else:
    print("Incorrect. This is the definition of:", words[pick])
