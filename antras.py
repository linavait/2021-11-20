def compute_bmi(weight, height, sportuoja=False):
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = "underweight"
    elif bmi > 25 and not sportuoja:
        result = "overweight"
    else:
        result = "normal"
    return result


if __name__ == '__main__':
    user_weight = float(input('Your weight [kg]: '))
    user_height = float(input('Your height [m]: '))
    user_result = compute_bmi(user_weight, user_height)
    print(f"You are {user_result}")


