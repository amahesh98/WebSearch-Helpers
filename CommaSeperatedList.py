def separate(mode:str):
  nextLine = input("Enter the first set of words (-1 to quit):")
  wordList = []
  while(nextLine!='-1'):
    splitLine = nextLine.split()
    for word in splitLine:
      if mode == 'int':
        wordList.append(float(word))
      else:
        wordList.append(word.lower())
    nextLine = input()
  
  return wordList

if __name__ == "__main__":
  print(separate('int'))
