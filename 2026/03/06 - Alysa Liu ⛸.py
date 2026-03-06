def calculate_score(elements):

  tes = 0

  for item in elements:

    item[2].remove(min(item[2]))
    item[2].remove(max(item[2]))

    avarage_goe = sum(item[2]) / len(item[2])
    tes += item[1] + (avarage_goe * 0.1 * item[1])
  
  return round(tes,1)