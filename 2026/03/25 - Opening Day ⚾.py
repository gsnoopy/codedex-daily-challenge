def streak_counter(games):
    
  sequence = 0
  sequences = []
  
  if "L" not in games:
    return games.count("W")

  for game in games:
    if game == 'W':
      sequence += 1
    if game == 'L':
      sequences.append(sequence)
      sequence = 0
      
  return max(sequences)