# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time #needed to calculate the time

#create a function that will search the array using linear search
def linearSearch(array, item):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return -1


#initialize a function that will use binary search
def binarySearch(array, item):
    print("Hi")


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    #load the menu 
    loop = True 
    while loop:
        print("Main Menu")
        userInp = input("Enter the number \n 1. Spell Check a Word (Linear Search) \n 2. Spell Check a Word (Binary Search)\n 3. Spell Check Alice In Wonderland (Linear Search) \n 4. Spell Check Alice In Wonderland (Binary Search) \n 5. Exit\n")
        
        if userInp == "1":
            word = input("Enter a word: ").lower()
            linearSearch(dictionary, word)

        elif userInp == "2":
            word = input("Enter a word: ").lower()
            binarySearch(dictionary, word)

        elif userInp == "3":
            linearSearch(dictionary, word)

        elif userInp == "4":
            linearSearch(dictionary, word)

        elif userInp == "5":
            print("Program closed")
            quit()

        else:
            print("Invalid Response")

    
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()



# Call main() to begin program
main()
