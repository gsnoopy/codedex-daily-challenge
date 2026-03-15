def decode_message(message, shift):
  
  decoded = ""

  for char in message:
    if char == " ":
        decoded += " "
    else:
      decoded += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

  return decoded