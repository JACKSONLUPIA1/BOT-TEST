wordArr = []
userGuessArr = []
debugArr = []
green = []
yellow = []
null = []

greenPos = []
yellowPos = []

wordGuess = "zebra"

with open('words.txt') as f:
    for line in f:
        wordArr.append(line.strip())
        
def getPos(word):
    test_str = '|||||'
    for letter in word:
        pos = int(input("What is the position of letter " + letter + ": "))
        test_str = test_str[:pos] + letter + test_str[pos + 1:]
    print(test_str)
    return test_str
        
def getUserInput():
    greenLen = int(input("How many green letters: "))
    for i in range(greenLen):
        letterGreen = str(input("Letter: "))
        green.append(letterGreen.lower())
    # yellowLen = int(input("How many yellow letters: "))
    # for i in range(yellowLen):
    #     letterYellow = str(input("Letter: "))
    #     yellow.append(letterYellow.lower())
    # nullLen = int(input("How many letters aren't in the word: "))
    # for i in range(nullLen):
    #     letterNull = str(input("Letter: "))
    #     null.append(letterNull.lower())
    green_array_str = ''.join(map(str, green))
    return green_array_str

def searchWords(str_test):
    # pos_word = str_test.indexOf()
    pos_letter = []
    length = len(str_test)
    if length == 5:
        for letter in str_test:
            if letter != '|':
                print(str_test.index(letter))
                pos_letter.append(letter + str(str_test.index(letter)))
    print(pos_letter)
    for word in wordArr:
        for i in range(len(pos_letter)):
            if pos_letter[i][0] in word:
                if pos_letter[i][1] == str(word.index(pos_letter[i][0])):
                    print(word)
                
    # for word in wordArr:
    #     if length == 1:
    #         if str_test in word[0]:
    #             print("1: " + word)
    #     if length == 2:
    #         if str_test in word[0:2]:
    #             print("2: " + word)
    #     if length == 3:
    #         if str_test in word[0:3]:
    #             print("3: " + word)
    #     if length == 4:
    #         if str_test in word[0:4]:
    #             print("4: " + word)

green_test = getUserInput()
new_green_str = getPos(green_test)
searchWords(new_green_str)


