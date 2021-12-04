"""Create a function that takes a list of integers and returns what the
smallest number is in.
Do not use built-in functions.
eg for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
the smallest element is found at this index in this list."""


if __name__ == '__main__':
    list1 = [42, 13, 56, 7, 12, 3, 85]
    place = 0
    min_ele = list1[0]
    for i in list1:
        if min_ele > i:
            min_ele = i
            min_ele_place = place
        place = place + 1
    print(min_ele_place)