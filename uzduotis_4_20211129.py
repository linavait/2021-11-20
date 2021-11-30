if __name__ == "__main__":
    word = input("your word: ")
    if word == word[::-1]:
        print("word is palindrome")
    else:
        print("word is not palindrome")
