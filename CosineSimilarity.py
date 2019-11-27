import math

# cos(D1, Q) = dot_product(TFIDF1, TFIDFq) / sqrt(sum(TFIDF1^2) * sum(TFIDFq^2))
def cosineSimilarity(termWeights1, termWeights2,):
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

if __name__ == "__main__":
  tfidf_q1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 9.0, 0.0, 0.0, 4.5, 0.0]
  tfidf_d2 = [0.0, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  tfidf_d4 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 9.0, 0.0, 4.5, 0.0]
  tfidf_d5 = [0.0, 0.0, 0.0, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.0, 0.0, 9.0, 0.0, 0.0]
  tfidf_d6 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0]
  tfidf_d8 = [0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

  print(f"D2: {cosineSimilarity(tfidf_q1, tfidf_d2)}")
  print(f"D4: {cosineSimilarity(tfidf_q1, tfidf_d4)}")
  print(f"D5: {cosineSimilarity(tfidf_q1, tfidf_d5)}")
  print(f"D6: {cosineSimilarity(tfidf_q1, tfidf_d6)}")
  print(f"D8: {cosineSimilarity(tfidf_q1, tfidf_d2)}")
  
