# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time #needed to calculate the time
import math #needed for binary search

#create a function that will search the array using linear search
def linearSearch(array, item):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return -1


#create a function that will search the array using binary search
def binarySearch(array, item):
    #set variables
    li = 0
    ui = len(array) - 1
   
    while li <= ui:
        mi = math.floor((li + ui)/2)
        if item == array[mi]:
            return mi
        elif item < array[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    return -1


#create a function that will search for the user's words in the dictionary
def wordSearch(searchFunction, array, item): 
    startTime = time.perf_counter()
    results = searchFunction(array, item)
    endTime = time.perf_counter()
     #check to see the results
    if results != -1:
        print(item + " is IN the dictionary at position " + str(results) + " (" + str(endTime - startTime) + " seconds)")
    else:
        print(item + " NOT in the dictionary" + " (" + str(endTime - startTime) + " seconds)")


#Create a function that will match words from AIW with the dictionary
def aliceSearch(searchFunction, array, reference):
    count = 0
    startTime = time.perf_counter()
    for x in reference:
        x.lower()
        results = searchFunction(array, x)
        if results == -1:
            count+=1
    endTime = time.perf_counter()
    print("Numbers of words not found in dictionary: " + str(count) + " (" + str(endTime - startTime) + " seconds)" )


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
            wordSearch(linearSearch, dictionary, word)

        elif userInp == "2":
            word = input("Enter a word: ").lower()
            wordSearch(binarySearch, dictionary, word)

        elif userInp == "3":
            aliceSearch(linearSearch, dictionary, aliceWords)
                
        elif userInp == "4":
            aliceSearch(binarySearch, dictionary, aliceWords)

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

