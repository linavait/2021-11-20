#patikrinti ar pirminis skaičius.pirminis(the number is prime or not)
if __name__ == '__main__':
    ele = 11
if ele > 0:
    for i in range(2, (ele//2)):
        if (ele % i) == 0:
            print(False, ele, "is not prime number")
            break
        else:
            print(True, ele, "is prime number")

