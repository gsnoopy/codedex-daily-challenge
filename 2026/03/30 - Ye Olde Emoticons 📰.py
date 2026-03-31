def emoticons_mood(message):

  happy = [":)", ":p", "xd", ":3", "<3", "\\m/"]
  sad = [":(", ":'(", "t(-.-t)"]
  words = message.lower().split()
  count = 0

  for item in words:
    for h in happy:
      count += item.count(h)
    for s in sad:
      count -= item.count(s)

  return count