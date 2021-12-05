if __name__ == "__main__":
  from collections import Counter
  text = "vienas du du trys trys trys keturi keturi keturi keturi penki penki penki penki penki sesi sesi sesi sesi sesi sesi septyni septyni septyni septyni septyni septyni septyni"
  words = text.split()
#print(words)
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word]+=1
    else:
      word_counts[word]=1
#print(word_counts)
  k = Counter(word_counts)
  top5_words = k.most_common(5)
  for t5,i in top5_words:
    print(t5)
