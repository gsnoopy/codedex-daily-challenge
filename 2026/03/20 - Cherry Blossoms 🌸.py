def cherry_blossoms(temps):

  for i in range(4, len(temps)):
    janela = temps[i-4:i+1]
    media = sum(janela) / 5
    if media > 15:
      return i + 1

  return -1