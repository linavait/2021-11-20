if __name__ == '__main__':
    number = input("enter number: ")
    number_names = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
                    "7": "seven", "8": "eight", "9": "nine"}
    if number.isnumeric():
        number_list = list(number)
        rez = ""
        for i in number_list:
            rez = rez + number_names[i] + " "
        print(rez)
    else:
        print("not number!")







