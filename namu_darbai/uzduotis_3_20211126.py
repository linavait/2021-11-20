"""Create a function that checks that the number given in the argument is
prime. The function should take a numeric value and return a logical
value of True / False.
E.g.
For 11 the function will return True, for 12 -> False."""


if __name__ == "__main__":
    n = int(input("Enter a number:"))
    if n > 1:
        for i in range(2, n // 2):
            if (n % i) == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not prime number")