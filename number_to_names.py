# function
def number_to_words(number):
  number_names ={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
  if number.isnumeric():
    number_list = list(number)
    rez = ""
    for i in number_list:
      rez = rez + number_names[i] + " "
    print(rez)
  else:
    print("entered not number!!!")
if __name__ == '__main__':
    number_entered = input("ivesk numeri: ")
    user_result = number_to_words(number_entered)
    print(user_result)
