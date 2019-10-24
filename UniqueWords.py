def getUniqueWords(wordList:[str]):
  output = []
  for word in wordList:
    if word not in output:
      output.append(word)
  output.sort()
  return output

if __name__ == '__main__':
  nextLine = input("Enter the first set of words (-1 to quit):")
  wordList = []
  while(nextLine!='-1'):
    splitLine = nextLine.split()
    for word in splitLine:
      wordList.append(word)
    nextLine = input("Enter the first set of words (-1 to quit):")

  uniqueList = getUniqueWords(wordList)
  for word in uniqueList:
    print(word)