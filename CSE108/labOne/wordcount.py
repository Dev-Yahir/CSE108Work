import re

word = input("Enter a word: ")

occur = 0 # counter for occurrences of the word given by the user

with open('PythonSummary.txt', 'r') as file: # open the file in read mode
    for line in file:
        words = re.findall(r'\b' + re.escape(word) + r'\b', line, re.IGNORECASE) #Clear the word that was read in of punctuation and determines its the same as the word given by the user
        if words:
            occur += len(words) #word matches so our counter is incremented by the number of occurrences of the word in the line

print("The word " + word + " occurs " + str(occur) + " times.")