def lucky_river(river, hours):

  n = len(river)
  final = ['💧'] * n

  for i, item in enumerate(river):
    if item == '☘️':
      end = min(i + hours, n - 1)
      for j in range(i, end + 1):
        final[j] = '☘️'

  return final