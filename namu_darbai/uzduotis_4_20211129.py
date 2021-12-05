"""Create a function that checks that the string given as an argument is a
palindrome (ie read backwards and forwards is exactly the same, eg
"kayak", "madam")."""
if __name__ == "__main__":
    word = input("your word: ")
    if word == word[::-1]:
        print("word is palindrome")
    else:
        print("word is not palindrome")
