"""Create a function that takes a list of integers and returns what the
smallest number is in.
Do not use built-in functions.
eg for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
the smallest element is found at this index in this list."""


list1 = [42, 13, 56, 7, 12, 3, 85]
min_ele = list1[0]
for i in list1:
    if int(i) < min_ele:
        min_ele = int(i)

if __name__ == '__main__':
    print(list1.index(min_ele))