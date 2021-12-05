"""Create a function that will calculate the number of upper and lower case
letters in a string.
eg for: "The quick Brown Fox"
expected result:
Number of uppercase letters: 3, number of lowercase letters : 13
Hint: use a loop, conditional statement, and appropriate methods for the
string."""


if __name__ == "__main__":
    string = ("The quick Brown Fox")
    count1 = 0
    count2 = 0
    i = 0
    for i in string:
        if i.islower():
            count1 = count1 + 1
        elif i.isupper():
            count2 = count2 + 1
    print("The number of lowercase characters is:", count1)
    print("The number of uppercase characters is:", count2)