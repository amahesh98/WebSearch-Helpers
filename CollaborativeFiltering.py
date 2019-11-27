import math

#Returns a converted list that centers the users values at 0 (0 is the average for all users, unknown = 0 and has no penalty)
#Used so that unknown values are not weighted negatively
def convertListToZeroAverageList(userValues:[float]):
  sumVal = 0.0
  count = 0.0
  for i in range(0, len(userValues)):
    if userValues[i] != 0:
      sumVal+=userValues[i]
      count+=1.0
  avg = sumVal / count
  output = []
  for i in range(0, len(userValues)):
    if userValues[i]!=0:
      output.append(userValues[i]-avg)
    else:
      output.append(0)
  
  return output

# cos(D1, Q) = dot_product(TFIDF1, TFIDFq) / sqrt(sum(TFIDF1^2) * sum(TFIDFq^2))
def cosineSimilarity(termWeights1:[float], termWeights2:[float]):
  if len(termWeights1) != len(termWeights2):
    print("Error: Lengths of weight vectors do not match")
    return -1

  top = 0.0
  sumSquared1 = 0.0
  sumSquared2 = 0.0
  for i in range(0, len(termWeights1)):
    top+=termWeights1[i]*termWeights2[i]
    sumSquared1+=pow(termWeights1[i], 2)
    sumSquared2+=pow(termWeights2[i], 2)
  
  bottom = math.sqrt(sumSquared1*sumSquared2)
  return top/bottom

#Pearson Correlation Coefficient Using Cosine Similarity
def PearsonCorrelation(user1Values:[float], user2Values:[float]):
  user1Values = convertListToZeroAverageList(user1Values)
  user2Values = convertListToZeroAverageList(user2Values)

  return cosineSimilarity(user1Values, user2Values)

#Predicts an unknown value given the full dataset
def predictValue(predictionListIndex:int, valueIndex:int, allUserLists:[[float]], printStatements = False):
    predictionList = allUserLists[predictionListIndex]
    totalSimilarity = 0.0
    averagedAndWeightedRating = 0.0
    for otherList in allUserLists:
      #Automatically skips predictionList b/c checks for 0
      if(otherList[valueIndex] != 0):
        similarity = PearsonCorrelation(predictionList, otherList)
        printStatements and print(f"Similarity: {similarity}")
        if similarity > 0:
          averagedAndWeightedRating += otherList[valueIndex]*similarity
          printStatements and print(f"Contribution: {otherList[valueIndex]*similarity}")
          totalSimilarity += similarity
    printStatements and print(f"averagedRating: {averagedAndWeightedRating}") and print(f"Total Similarity: {totalSimilarity}")
    
    return averagedAndWeightedRating / totalSimilarity

if __name__ == "__main__":
  # A = [4,0,0,5,1,0,0]
  # B = [5,5,4,0,0,0,0]
  # C = [0,0,0,2,4,5,0]
  # print(f"Sim A and B: {PearsonCorrelation(A, B)}")
  # print(f"Sim A and C: {PearsonCorrelation(A, C)}")
  A = [4,1,3,5]
  B = [0,5,4,0]
  C = [5,4,2,0]
  D = [2,4,0,3]
  E = [3,4,5,0]

  fullList = [A, B, C, D, E]

  print(f"B1: {predictValue(1, 0, fullList)}")
  print(f"B4: {predictValue(1, 3, fullList)}")
  print(f"C4: {predictValue(2, 3, fullList)}")
  print(f"D3: {predictValue(3, 2, fullList)}")
  print(f"E4: {predictValue(4, 3, fullList)}")