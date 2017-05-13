# Tatum Hawkins
# LIS 452 Final Project

import random

def vocab_game(given_chapter):
    # Read in the chapter requested by the user.
    ch_num = str(given_chapter)
    chapter_name = "Chapter "+ch_num+".txt"
    #print(chapter_name)
    inchapter = open(chapter_name, 'r')
    chapter = inchapter.readlines()

    # Find the glossary and ignore the rest of the chapter.
    # Should be between the line ending with "Glossary" and the line ending with "Exercises".

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
    #vocabs = []
    # Separate - I wasn't actually using the list of tuples anywhere.
    words = []
    defs = []

    for each in range(gloss_start, gloss_end, 2):
        next_pair = (chapter[each].strip(), chapter[each+1].strip())
        #vocabs.append(next_pair)
        words.append(chapter[each].strip())
        defs.append(chapter[each+1].strip())

    # Find out how many vocab words are in the chapter.
    num_vocabs = len(words)

    # This is list masks the words and defs lists so that they can be reused and their order doesn't get wonky.
    # Instead I've got a list of indices that I can remove as we go through without moving the initial positions
    # of things in the words and defs. May not be necessary, but it makes me feel more comfortable at the moment.
    num_of_words=[]
    num_of_words.extend(range(num_vocabs))
    print(num_of_words)

    print("DIRECTIONS: Read the definition, then enter the corresponding vocabulary word. "
          "Remember, it must be spelled correctly to receive any credit.\n")

    missed_words = []
    score = 0

    for each in range(num_vocabs):

        # Select a random vocab index for the quiz question and removes it from the list at the same time, so
        # that word doesn't get reused in the same quiz.
        pick = num_of_words.pop(random.randint(0, len(num_of_words)-1)) # Again with the 0 vs 1 thing
        #print(pick)
        print(words[pick], "\n")
        #print(num_of_words)

        # Interact with the user. Give a definition and get a response.
        # Check to see if the word is correct.
        # How to go through all the words using random, without repeating... How does pop work?
        # Maybe make a list of the numbers and then pick a random entry and then pop it out? So,
        # then random would be for the positioin in the number list rather than the vocab list.
        # That way the changing positions doesn't lead to repeating vocab words...

        # Playing with the quiz part.

        print("Def:", defs[pick], "\n")
        response = input("\t This is the definition of what vocabulary word or phrase? ")
        if response == words[pick]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. This is the definition of:", words[pick])
            missed_words.append(words[pick])


    print("\n\nYOU GOT", score, "WORDS CORRECT.")
    print("The words you need to practice are:", missed_words)


scope = eval(input("What vocabulary would you like to practice? \n[Enter 0 for all vocab, "
              "a number 1-27 for a specific chapter, or -1 to quit.]: "))

if scope == 0:
    print("All vocab")
    vocab_game(scope)
    print("Good luck on your test! Good-bye.")

elif 0 < scope < 28:
    print("Chapter number is:", scope)
    vocab_game(scope)
    print("Good luck on your test! Good-bye.")

else:
    print("Good luck on your test! Good-bye.")
