def tweet_balance(tweet):
  words = tweet.split()
  balance = 0

  for item in words:
    if item.startswith("@"):
      balance += 20
    elif item.startswith("http://") or item.startswith("https://"):
      balance += 23
    else:
      for char in item:
        if ord(char) > 10000:
          balance += 2
        else:
          balance += 1
          
  if len(words) > 1:
    balance += len(words) - 1
  
  return 140 - balance
    