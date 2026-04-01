def longest_streak(progress):

  sequences = []
  sequence = 0

  for i in range(len(progress)):
      
    if progress[i] == "✅":
      sequence += 1
    else:
      sequences.append(sequence)
      sequence = 0

  sequences.append(sequence)
  
  return max(sequences)