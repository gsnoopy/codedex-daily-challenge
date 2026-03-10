def find_unique_words(transcript):
  
    transcript = transcript.lower()
    punctuation = ".,!?;:'\""

    for item in punctuation:
        transcript = transcript.replace(item, "")
  
    words = transcript.split()
    words = list(set(words))

    return len(words)