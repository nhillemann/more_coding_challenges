'''
Sloth Bytes Weekly Challenge - Calendar Week 06 2025

Task: Create a function that returns true if two lines rhyme and false otherwise.
For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.

Examples:
doesRhyme("You're built like a seat", "I bet you like to eat")
output = True
doesRhyme("You are off to the races", "a splendid day.")
output = False

Notes:
Case insensitive.
Here we are disregarding cases like "thyme" and "lime".
We are disregarding cases like "away" and "today" (which technically rhyme, even though they contain different vowels).
'''

# My solution:
import re

def doesRhyme():
    # Input: two lines string format to compare
    line1_input = input("Enter your first line of text: ")
    line2_input = input("Enter a second line of text: ")

    def get_last_word_vowels(line):
        # 1st: Remove punctuation and split string into words
        words = re.findall(r'\b\w+\b', line.lower())
        last_word = words[-1] if words else ""

        # 2nd: Extract vowels from last word for comparison
        vowels = [char for char in last_word if char in 'aeiou']
        return vowels

    # Getting Vowels from last word of each line
    vowels1 = get_last_word_vowels(line1_input)
    vowels2 = get_last_word_vowels(line2_input)

    # Comparing the vowels, returning a boolean
    return vowels1 == vowels2

if __name__ == '__main__':
    result = doesRhyme()
    print(result)



