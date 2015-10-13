__author__ = 'Jeffrey'


def get_user_name():
    user_name = str(input("Please enter your name."))
    name_file = open("name.txt", mode="w", encoding="utf-8")
    name_file.write(user_name)
    name_file.close()

get_user_name()


def printing_name_file():
    name_file = open("name.txt", mode="r")
    name = name_file.read().strip()
    print("Your name is {}".format(name))
    name_file.close()

printing_name_file()


def printing_them_numbers():
    num_total = 0
    numbers_file = open("numbers.txt", mode="r", encoding="utf-8")
    for line in numbers_file:
            value = int(line)
            num_total += value
            print(num_total)
    numbers_file.close()

printing_them_numbers()
