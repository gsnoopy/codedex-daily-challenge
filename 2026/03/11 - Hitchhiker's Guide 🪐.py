from itertools import combinations

def minimum_components(components):
  total = 0
  
  for i in range(1, len(components) + 1):
      for j in combinations(components, i):
          total = sum(j)
          if total == 42:
            return len(j)
            
  return -1