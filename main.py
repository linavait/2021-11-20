# mano svorio indeksas

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# TODO : pataisyk
def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.4:
        result = "underweight"
    elif bmi > 25:
        result = "overweight"
    else:
        result = "normal"
    return result


if __name__ == '__main__':
    user_weight = float(input('your weight [kg]: '))
    user_height = float(input('Your height [m]: '))
    user_result = compute_bmi(user_weight, user_height)
    print(f'you are {user_result}')



