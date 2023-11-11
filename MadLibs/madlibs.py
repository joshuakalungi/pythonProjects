# Mad Libs is a word game where one player prompts others for a list of words
# to substitute for blanks in a story before reading it aloud. 
#The result is often a funny and sometimes nonsensical story due to the unpredictable
#input provided by the players.

# In a Python Mad Libs project, you can create a program that prompts the user to 
# enter different types of words (nouns, verbs, adjectives, etc.) and then inserts 
# those words into a pre-written story template, creating a unique and often humorous 
# narrative. Here's a simple example to help you understand the concept:###

# Prompt user for words
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb1 = input("Enter a verb: ")
noun3 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adjective3 = input("Enter another adjective: ")
noun4 = input("Enter another noun: ")
noun5 = input("Enter another noun: ")
adjective4 = input("Enter another adjective: ")
place = input("Enter a place: ")
noun6 = input("Enter another noun: ")
verb3 = input("Enter another verb: ")
adjective5 = input("Enter another adjective: ")
noun7 = input("Enter another noun: ")
verb4 = input("Enter another verb: ")
adjective6 = input("Enter another adjective: ")
noun8 = input("Enter another noun: ")
verb5 = input("Enter another verb: ")
adjective7 = input("Enter another adjective: ")
noun9 = input("Enter another noun: ")
verb6 = input("Enter another verb: ")
noun10 = input("Enter another noun: ")
noun11 = input("Enter another noun: ")
noun12 = input("Enter another noun: ")


# Mad Libs Story Template

story_template = f"""
Once upon a time in the magical land of {adjective1} {noun1}, there lived a {adjective2} {noun2}. 
This peculiar {noun2} had a unique ability to {verb1} with {noun3} and {verb2} with {adjective3} {noun4}.
One day, as the {noun2} was {verb3} in the {adjective4} {place}, a mysterious {noun5} appeared.

The {noun5} granted the {noun2} three wishes. For the first wish, the {noun2} wished for a {adjective5} {noun6}. 
For the second wish, the {noun2} wanted to {verb4} through the {adjective6} {noun7}. 
And for the final wish, the {noun2} wished for endless {noun8} and {verb5}.

With the wishes granted, the {noun2} found themselves in a world filled with {adjective7} {noun9} and {verb6} {noun10}. 
They lived happily ever after, surrounded by the enchanting {noun11} and the soothing sound of {noun12}.
"""


# # Substitute user input into the story
# mad_lib_story = story_template.format(
#     adjective1=adjective1, noun1=noun1, adjective2=adjective2, noun2=noun2,
#     verb1=verb1, noun3=noun3, verb2=verb2, adjective3=adjective3, noun4=noun4,
#     noun5=noun5, adjective4=adjective4, place=place, noun6=noun6, verb3=verb3,
#     adjective5=adjective5, noun7=noun7, verb4=verb4, adjective6=adjective6,
#     noun8=noun8, verb5=verb5, adjective7=adjective7, noun9=noun9, verb6=verb6,
#     noun10=noun10, noun11=noun11, noun12=noun12
# )

# Display the Mad Libs story
print("\nYour Mad Libs Story:\n" + story_template)
