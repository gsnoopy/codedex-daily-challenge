def leaky_pipe(volume, leak, hours, threshold):

  for i in range(hours):
    volume = volume * (1 - (leak / 100))
    
    if volume < threshold:
      return -1
      
  return round(volume, 2)