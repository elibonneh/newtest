def divide_by_2():
    number = input("enter the number: ")
    print(int(number) / 2)


def plus_function(num_1, num_2):
    return num_1 + num_2


def strings_connector(str_1, str_2):
    return str_1 + " " + str_2


if __name__ == '__main__':
    number_result = plus_function(5, 6)
    print(number_result)

    string_result = strings_connector("hello", "world")
    print(string_result)