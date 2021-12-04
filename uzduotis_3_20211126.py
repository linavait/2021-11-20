"""Create a function that checks that the number given in the argument is
prime. The function should take a numeric value and return a logical
value of True / False.
E.g.
For 11 the function will return True, for 12 -> False."""


if __name__ == '__main__':
    ele = 11
if ele > 0:
    for i in range(2, (ele//2)):
        if (ele % i) == 0:
            print(False, ele, "is not prime number")
            break
        else:
            print(True, ele, "is prime number")

