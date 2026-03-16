def oscar_pool(predictions):

  winners = [
    'One Battle After Another',
    'Michael B. Jordan',
    'Jessie Buckley',
    'Paul Thomas Anderson'
  ]

  accuracy = {}

  for prediction in predictions:
    user = prediction[0]
    guesses = prediction[1:]

    corrects = 0

    for guess in guesses:
      if guess in winners:
        corrects += 1

    accuracy[user] = round(corrects / len(winners), 2)

  max_accuracy = max(accuracy.values())

  winners_users = [user for user, acc in accuracy.items() if acc == max_accuracy]

  if len(winners_users) > 1:
    return "Tie"
  else:
    return winners_users[0]