# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    #load the menu 
    loop = true 
    while loop:
        print("Main Menu")
        userInp = input("Enter the number \n 1. Spell Check a Word (Linear Search) \n 2. Randomize Grades \n 3. Stats \n 4. Count Honors \n 5. Exit\n")
        
        if userInp == "1":
            displayGrades()

        elif userInp == "2":
            createGrades()
            print("Grades added")

        elif userInp == "3":
            stats()

        elif userInp == "4":
            honors()

        elif userInp == "5":
            print("Program closed")
            sys.exit()

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
