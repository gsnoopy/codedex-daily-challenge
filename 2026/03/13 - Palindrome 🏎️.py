def check_palindrome(sequence):
    
  sequence = sequence.replace(" ", "")
  inverted = sequence[::-1]
  
  if sequence.lower() == inverted.lower():
      return True
  else:
     return False
