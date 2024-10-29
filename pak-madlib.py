# Madlib Assignment
# Pak King Lee
# Oct 22, 2024

import random

# pick random word from wordlist provided
def pick_word(keyword, lines_num):
    # find the keyword and output the following lines as a list
    start_index = textfile.index(keyword) + 1
    wordlist = textfile[start_index:start_index + lines_num]
    # pick random word from list
    word_chosen = random.choice(wordlist)
    # remove newline (\n)
    clean_text = word_chosen.strip()
    return clean_text

# ask user which rhyme to pick and foolproof
print('''
Which rhyme do you want to pick?
1. Jack and Jill
2. Hey diddle diddle
''')
rhyme = "0"
while rhyme != "1" and rhyme != "2":
    rhyme = input('''Please pick an option: ''')
    if rhyme != "1" and rhyme != "2":
        print('''That option is not avaliable, pick again.''')

# ask user how to fill in madlib and foolproof
print('''
How do you want to fill in the madlib?
1. On your Own
2. Original
3. Random
''')
fillin_option = "0"
while fillin_option != "1" and fillin_option != "2" and fillin_option != "3":
    fillin_option = input('''Please pick an option: ''')
    if fillin_option != "1" and fillin_option != "2" and fillin_option != "3":
        print('''That option is not avaliable, pick again.''')

# set the words in the madlib if user choose to fill in on their own
if fillin_option == "1":
    if rhyme == "1":
        word_one = input("Name (Person 1): ")
        word_two = input("Name (Person 2): ")
        word_three = input("Place: ")
        word_four = input("Noun (something to fetch): ")
        word_five = input("Verb ending in -ed: ")
        word_six = input("Body part: ")
        word_seven = input("Verb ending in -ing: ")
    elif rhyme == "2":
        word_one = input("Exclaimation word: ")
        word_two = input("Animal: ")
        word_three = input("Musical instrument: ")
        word_four = input("Animal 2: ")
        word_five = input("Adjective: ")
        word_six = input("Verb ending in -ed: ")
        word_seven = input("Kitchen item: ")
    
        
# set the words in the madlib if user choose to see original
elif fillin_option == "2":
    if rhyme == "1":
        word_one = "Jack"
        word_two = "Jill"
        word_three = "hill"
        word_four = "pail of water"
        word_five = "fell down"
        word_six = "crown"
        word_seven = "tumbling"
    elif rhyme == "2":
        word_one = "Hey"
        word_two = "cat"
        word_three = "fiddle"
        word_four = "cow"
        word_five = "little"
        word_six = "laughed"
        word_seven = "spoon"
        
# set the words in the madlib if user choose see original
elif fillin_option == "3":
    if rhyme == "1":
        # open the correct files
        textfile = open('rhyme1.txt','r')
        textfile = textfile.readlines()
        word_one = pick_word('word_1\n', 10)
        word_two = pick_word('word_2\n', 10)
        word_three = pick_word('word_3\n', 10)
        word_four = pick_word('word_4\n', 10)
        word_five = pick_word('word_5\n', 10)
        word_six = pick_word('word_6\n', 10)
        word_seven = pick_word('word_7\n', 10)
    elif rhyme == "2":
        # open the correct files
        textfile = open('rhyme2.txt','r')
        textfile = textfile.readlines()
        word_one = pick_word('word_1\n', 10)
        word_two = pick_word('word_2\n', 10)
        word_three = pick_word('word_3\n', 10)
        word_four = pick_word('word_4\n', 10)
        word_five = pick_word('word_5\n', 10)
        word_six = pick_word('word_6\n', 10)
        word_seven = pick_word('word_7\n', 10)

# print the rhymes!
if rhyme == "1":
    print(f'''
    {word_one} and {word_two} went up the {word_three},
    To fetch a {word_four}.
    {word_one} {word_five} and broke his {word_six},
    And {word_two} came {word_seven} after.
    ''') 

elif rhyme == "2":
    print(f'''
    {word_one} diddle diddle,
    The {word_two} and the {word_three},
    The {word_four} jumped over the moon;
    The {word_five} dog {word_six}
    To see such sport,
    And the dish ran away with the {word_seven}.
    ''')