import streamlit as st
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

# Add tabs
tab1, tab2, tab3 = st.tabs(["Madlib Options", "Fill in the blanks", "Result!"])

with tab1:
    st.title("🎈 Pick your method to make the madlib!")
    # ask user which rhyme to pick
    rhyme = st.radio("Which rhyme do you want to pick?", ["Jack and Jill", "Hey diddle diddle"])

    # ask user how to fill in madlib and foolproof
    fillin_option = st.radio("How do you want to fill in the madlib?", ["Original", "On your Own", "Random"])

with tab2:
    # set the words in the madlib if user choose to fill in on their own
    if fillin_option == "On your Own":
        if rhyme == "Jack and Jill":
            word_one = st.text_input("Name (Person 1): ")
            word_two = st.text_input("Name (Person 2): ")
            word_three = st.text_input("Place: ")
            word_four = st.text_input("Noun (something to fetch): ")
            word_five = st.text_input("Verb ending in -ed: ")
            word_six = st.text_input("Body part: ")
            word_seven = st.text_input("Verb ending in -ing: ")
        elif rhyme == "Hey diddle diddle":
            word_one = st.text_input("Exclaimation word: ")
            word_two = st.text_input("Animal: ")
            word_three = st.text_input("Musical instrument: ")
            word_four = st.text_input("Animal 2: ")
            word_five = st.text_input("Adjective: ")
            word_six = st.text_input("Verb ending in -ed: ")
            word_seven = st.text_input("Kitchen item: ")
        
            
    # set the words in the madlib if user choose to see original
    elif fillin_option == "Original":
        if rhyme == "Jack and Jill":
            word_one = "Jack"
            word_two = "Jill"
            word_three = "hill"
            word_four = "pail of water"
            word_five = "fell down"
            word_six = "crown"
            word_seven = "tumbling"
        elif rhyme == "Hey diddle diddle":
            word_one = "Hey"
            word_two = "cat"
            word_three = "fiddle"
            word_four = "cow"
            word_five = "little"
            word_six = "laughed"
            word_seven = "spoon"
            
    # set the words in the madlib if user choose see original
    elif fillin_option == "Random":
        if rhyme == "Jack and Jill":
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
        elif rhyme == "Hey diddle diddle":
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

with tab3:
    # print the rhymes!
    if rhyme == "Jack and Jill":
        st.write(f'''
        {word_one} and {word_two} went up the {word_three},\n
        To fetch a {word_four}.\n
        {word_one} {word_five} and broke his {word_six},\n
        And {word_two} came {word_seven} after.\n
        ''') 

    elif rhyme == "Hey diddle diddle":
        st.write(f'''
        {word_one} diddle diddle,\n
        The {word_two} and the {word_three},\n
        The {word_four} jumped over the moon;\n
        The {word_five} dog {word_six}\n
        To see such sport,\n
        And the dish ran away with the {word_seven}.\n
        ''')
