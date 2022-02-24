# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time #needed to calculate the time

#initiliaze a function that will use linear search
def linearSearch(array, item):
    #create a variable to store current time
    currentTime = time.perf_counter()
    for i in range(len(array)):
        if array[i] == item:
            endTime = time.perf_counter()
            return print(item + " is IN dictionary and found in position" + str(array[i]) + " in" + str(endTime - currentTime) + " seconds")
        endTime = time.perf_counter()
        return print(item + " is NOT in dictionary and took " + str(endTime - currentTime) + " seconds")


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
