def calculate_sleep_debt(planned, actual):
  sleep_debt = 0
  sequency = 0
  max_sequency = 0

  for item, item2 in zip(planned, actual):
    sleep_debt += max(0, item - item2)

    if item > item2:
      sequency += 1
      max_sequency = max(max_sequency, sequency)
    else:
      sequency = 0

  sleep_debt += 1
  return sleep_debt, max_sequency