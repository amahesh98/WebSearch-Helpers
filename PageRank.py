def pageRank(pages:[str], links:[(str, str)], iterations:int, lambdaVar:float=0.0):
  pageLength = len(pages)
  currentRank_I = {}
  updatedRank_R = {}

  for page in pages:
    currentRank_I[page] = 1.0 / pageLength
  
  for k in range(0, iterations):
    for page in pages:
      updatedRank_R[page] = lambdaVar / pageLength

    for page in pages:
      Q =[]
      for link in links:
        if(link[0] == page):
          Q.append(link[1])

      if len(Q) > 0:
        for linkPage in Q:
          updatedRank_R[linkPage] += (1.0-lambdaVar)*currentRank_I[page]/len(Q)
      else:
        for linkPage in Q:
          updatedRank_R[linkPage] += (1.0-lambdaVar)*currentRank_I[page]/pageLength

    for rank in updatedRank_R:
      currentRank_I[rank] = updatedRank_R[rank]

    print(f"Current Rank at Iteration {k+1}:", currentRank_I)
  return currentRank_I

if __name__ == '__main__':
  A = 'A'
  B = 'B'
  C = 'C'
  D = 'D'
  pages = [A, B, C, D]
  links = [(A, B), (A, C), (B, A), (B, D), (C, A), (D, B), (D, C)]
  pageRank(pages, links, 3)