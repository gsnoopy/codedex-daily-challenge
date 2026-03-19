def upset_probability(matchups):
  result = []

  for matchup in matchups:
    valores = []
    
    for item in matchup:
      if isinstance(item, int): 
        valores.append(item)
    
    sup = min(valores)
    inf = max(valores)
        
    result.append(round(sup / (sup + inf), 2))
    
  return result