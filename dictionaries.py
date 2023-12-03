import string

def word_frequency(sentence):
  # Remove punctuation
  for c in string.punctuation:
    sentence = sentence.replace(c, ' ')

  # Convert to lowercase
  sentence = sentence.lower()

  # Split the sentence into words
  words = sentence.split()

  # Create a dictionary to store the word frequencies
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  return word_counts

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


