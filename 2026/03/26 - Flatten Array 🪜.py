def flatten(lista):
    
  result = []
  
  for value in lista:
    if isinstance(value, list):
      result.extend(flatten(value))
    else:
      result.append(value)
      
  return result