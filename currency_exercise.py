__author__ = 'Jeffrey'

def displaying_countries():
    countries_listed = []
    in_file = open('guitars.csv', 'r', newline='')
    for line in in_file:
        words = line.strip().split(",")
        new_guitar = Guitars(words[0], words[1], words[2])
        guitars_list.append(new_guitar)





def printing_name_file():
    name_file = open("name.txt", mode="r")
    name = name_file.read().strip()
    print("Your name is {}".format(name))
    name_file.close()