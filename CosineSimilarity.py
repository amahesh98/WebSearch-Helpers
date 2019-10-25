import math

# cos(D1, Q) = dot_product(TFIDF1, TFIDFq) / sqrt(sum(TFIDF1^2) * sum(TFIDFq^2))
def cosineSimilarity(termWeights1, termWeights2):
  if len(termWeights1) != len(termWeights1):
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

if __name__ == "__main__":
  termWeight1 = [0,1,0,0,0,0,0,0,0,0,0]
  termWeight2 = [0,1,0,0,2,2,0,0,0,1,0]
  termWeight3 = [0,0,2,0,0,0,2,2,2,0,0]
  termWeight4 = [2,0,0,2,0,0,0,0,0,0,2]

  termWeightQ_Rocchio = [2/9,4/9,2/9,2/9,4/3,2/3,2/9,2/9,2/9,4/9,2/9]
  termWeightQ2 = [0,1,0,0,2,2,0,0,0,1,0]
  termWeightQ_TFIDF = [0,0,0,0,2,0,0,0,0,0,0]
  print(cosineSimilarity(termWeight4, termWeightQ2))
  
