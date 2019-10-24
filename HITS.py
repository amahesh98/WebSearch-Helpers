def hasConnection(page1, page2, edges:[str, str]):
  for edge in edges:
    if(page1 == edge[0] and page2 == edge[1]):
      return True
  return False

def HITS(vertexes:[str], edges:[(str, str)], iterations:int):
  authority = [{}]
  hub = [{}]
  for page in vertexes:
    authority[0][page] = 1.0
    hub[0][page] = 1.0
  
  for i in range(1, iterations+1):
    authority.append({})
    hub.append({})
    for page in vertexes:
      authority[i][page] = 0.0
      hub[i][page] = 0.0
    
    zAuth = 0.0
    zHub = 0.0

    for page in vertexes:
      for otherPage in vertexes:
        if hasConnection(page, otherPage, edges):
          hub[i][page] += authority[i-1][otherPage]
          zHub += authority[i-1][otherPage]
        if hasConnection(otherPage, page, edges):
          authority[i][page] += hub[i-1][otherPage]
          zAuth += hub[i-1][otherPage]
    
    for page in vertexes:
      if zAuth > 0:
        authority[i][page] = authority[i][page] / zAuth
      if zHub > 0:
        hub[i][page] = hub[i][page] / zHub
    
    print(f"Hub at Iteration {i}: {hub[i]}")
    print(f"Auth at Iteration {i}: {authority[i]}")
  
  return authority[iterations], hub[iterations]
  
if __name__ == "__main__":
  A = 'A'
  B = 'B'
  C = 'C'
  vertexes = [A, B, C]
  edges = [(A, A), (A, B), (B, C), (C, A)]
  HITS(vertexes, edges, 50)