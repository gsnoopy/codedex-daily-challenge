def cuddly_kittens(kittens, limit):
  result = 0
  group = []

  for kitten in kittens:
    group.append(kitten)

    while max(group) - min(group) > limit:
      group.pop(0)

    result = max(result, len(group))

  return result