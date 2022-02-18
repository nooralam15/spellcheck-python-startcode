# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


#initalize a function that will linear search the dictionary
def linearDict():



#intitialize a function that will display the menu
def menu():
    #initialize variable
    loop = True
    #create a while loop that will loop through the menu
    while loop:
        #print the the title of the menu
        print("Main Menu")
        userInp = input("Enter the number \n 1. Spell Check a Word (Linear Search) \n 2. Spell Check a Word (Binary Search) \n 3. Spell Check Alice In Wonderland (Linear Search) \n 4. Spell Check Alice In Wonderland (Binary Search) \n 5. Exit\n")
        
        if userInp == "1":
            linearDict()

        elif userInp == "2":
            binaryDict()

        elif userInp == "3":
            linearAlice()

        elif userInp == "4":
            binaryAlice()

        elif userInp == "5":
            print("Program closed")
            sys.exit()

        else:
            print("Invalid Response")
menu()


# Call main() to begin program
main()
