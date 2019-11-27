import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 

def getUniqueWords(wordList:[str], porterStem:bool):
  output = []
  stopWords = set(stopwords.words('english'))
  porterStemmer = PorterStemmer()
  for word in wordList:
    if porterStem and word not in stopWords:
      word = porterStemmer.stem(word)
      if word not in output:
        output.append(word)
    elif word not in output:
      output.append(word)
  output.sort()
  return output

if __name__ == '__main__':
  nextLine = input("Enter the first set of words (-1 to quit):")
  wordList = []
  while(nextLine!='-1'):
    splitLine = nextLine.split()
    for word in splitLine:
      wordList.append(word.lower())
    nextLine = input("Enter the next set of words (-1 to quit):")

  uniqueList = getUniqueWords(wordList, porterStem=True)
  for word in uniqueList:
    print(word)
  print(f"Total unique word count: {len(uniqueList)}")