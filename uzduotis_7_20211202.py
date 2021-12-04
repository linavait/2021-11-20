"""Write a function that will return the 5 most common words from
Mickiewicz's work. https://pastebin.com/raw/aAHeW5Pt (copy and save
to a text file what you will find at this link).
Hint: use the open() function, split() method, dictionary and loop.
"""


if __name__ == "__main__":
    from collections import Counter
    with open('tekstas7_uzd.py', encoding='utf8') as f:
        lines = f.read()
        words = lines.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # print(word_counts)
    k = Counter(word_counts)
    top5_words = k.most_common(5)
    print(top5_words)
    # top5_words = sorted(word_counts, key=word_counts.get, reverse=True)[:5]
    # print(top5_words)
#     tik rusiuoja, ne skaiciuoja






