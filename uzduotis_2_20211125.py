#eilutėje reikia surasti mažiausią narį.
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