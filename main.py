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

def removeYellow():
  yellowLen = int(input("How many yellow letters: "))
  for i in range(yellowLen):
    letterYellow = str(input("Letter: "))
  for word in wordArr:
    if letterYellow not in word:
      print("REMOVED Y: " + word)
      wordArr.remove(word)
    
def getPos(word):
    test_str = '|||||'
    for letter in word:
        pos = int(input("What is the position of letter " + letter + ": "))
        test_str = test_str[:pos] + letter + test_str[pos + 1:]
    return test_str
        
def getUserInput():
    greenLen = int(input("How many green letters: "))
    for i in range(greenLen):
        letterGreen = str(input("Letter: "))
        green.append(letterGreen.lower())
    green_array_str = ''.join(map(str, green))
    return green_array_str

def searchWords(str_test):
    temp_arr = []
    temp_arr2 = []
    temp_arr3 = []
    temp_arr4 = []
  
    pos_letter = []
    length = len(str_test)
    if length == 5:
        for letter in str_test:
            if letter != '|':
                pos_letter.append(letter + str(str_test.index(letter)))
    # SEARCHES THE FIRST LETTER
    for word in wordArr:
      if pos_letter[0][0] in word:
        if pos_letter[0][1] == str(word.index(pos_letter[0][0])):
          temp_arr.append(word)

    # IF A SECOND LETTER IS VALID, IT WILL RUN THROUGH AGAIN
    if len(pos_letter) > 1:
      for word in temp_arr:
        if pos_letter[1][0] in word and pos_letter[1][1] == str(word.index(pos_letter[1][0])):
          # print("REMOVED 2 : " + word)
          temp_arr2.append(word)
          
    # THIRD LETTER TEST
    if len(pos_letter) > 2:
      for word in temp_arr2:
        if pos_letter[2][0] in word:
          if pos_letter[2][1] == str(word.index(pos_letter[2][0])):
            temp_arr3.append(word)
            
    if len(pos_letter) == 4:
      for word in temp_arr3:
        if pos_letter[3][0] in word:
          if pos_letter[3][1] == str(word.index(pos_letter[3][0])):
            temp_arr4.append(word)
            
    if len(pos_letter) == 1:
      return temp_arr
    if len(pos_letter) == 2:
      return temp_arr2
    if len(pos_letter) == 3:
      return temp_arr3
    if len(pos_letter) == 4:
      return temp_arr4


removeYellow()
print(wordArr)
green_test = getUserInput()
new_green_str = getPos(green_test)
print(searchWords(new_green_str))



 # yellowLen = int(input("How many yellow letters: "))
    # for i in range(yellowLen):
    #     letterYellow = str(input("Letter: "))
    #     yellow.append(letterYellow.lower())
    # nullLen = int(input("How many letters aren't in the word: "))
    # for i in range(nullLen):
    #     letterNull = str(input("Letter: "))
    #     null.append(letterNull.lower())
