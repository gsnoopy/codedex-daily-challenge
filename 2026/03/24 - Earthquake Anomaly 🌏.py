import statistics

def earthquake_anomaly(readings):
  
  if not readings:
    return []
  
  median = statistics.median(readings)
  rate = median * 1.5
  suspects = []
  
  for i, item in enumerate(readings):
    if item > rate:
      suspects.append(i)
      
  return suspects