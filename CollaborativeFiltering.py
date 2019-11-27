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
  

if __name__ == "__main__":
  A = [4,0,0,5,1,0,0]
  B = [5,5,4,0,0,0,0]
  C = [0,0,0,2,4,5,0]
  print(f"Sim A and B: {PearsonCorrelation(A, B)}")
  print(f"Sim A and C: {PearsonCorrelation(A, C)}")