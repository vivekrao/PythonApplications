"""
    Name generator
    Generates names with vowels/consonents/random according to user requirement
"""
import random
import string

# Define basic letter types
allLetters = string.ascii_lowercase
allVowels = "aeiou"
allConsonents = "bcdfghjklmnpqrstvwxyz"

"""
    Function to generate name
    @Param: input character to decide what type of letter to generate
    v == vowel
    c == consonent
    Any other letter == random
"""
def generateName(input) :
    result = ""
    if input == "v" :
        result = random.choice(allVowels)
    elif input == "c" :
        result = random.choice(allConsonents)
    else :
        result = random.choice(allLetters)

    return result

# Take input from user - total words and total letters in each word
t = int(input("How many words do you want?: "))
n = int(input("How many lettered name are you looking for?: "))

# Define local variables
name = ""
inputVar = ""

# Find out all the types of letters that the user wants
for _ in range(n) :
    inputVar += input("Enter v ~ vowel, c ~ consonent, any letter ~ random: ")

# Iterate t (total words) times
for _ in range(t) :
    # for each word call generator n(total letters) times
    for i in range(n) :
        name += generateName(inputVar[i])
    name += "\n" # Formatting output in separate lines

print(name)
