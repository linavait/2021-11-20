if __name__ == '__main__':
    my_list = [1, "text", None]
    print(my_list)
    print(type(my_list))
    print(id(my_list))
    print()

    my_list2 = my_list.copy()
    my_list2[1] = "new text"
    print(my_list2)
