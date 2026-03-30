def average_time(total, completed):
  hours, minutes, seconds = map(int, total.split(":"))
  time = (hours * 3600) + (minutes * 60) + seconds
  media = time / completed
  return round(media)