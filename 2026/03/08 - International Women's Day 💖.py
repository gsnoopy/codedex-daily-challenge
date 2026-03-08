def analyze(percentages):

  netchange = (percentages[-1] - percentages[0]) / (len(percentages) - 1)
  dips = 0

  first_three = sum(percentages[:3]) / len(percentages[:3])
  last_three = sum(percentages[-3:]) / len(percentages[-3:])

  if last_three == first_three:
      trend = "stagnating"
  elif last_three > first_three:
      trend = "improving"
  else:
      trend = "declining"

  for i in range(len(percentages) - 1):
    if percentages[i+1] < percentages[i]:
      dips += 1

  return round(netchange,4), trend, dips
