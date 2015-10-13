__author__ = 'Jeffrey'


class Guitars:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return ' "{:>25} {:>5} {:>9}" '.format(self.name, self.year, self.cost)

    def __lt__(self, other):
        return self.year < other.year


def sort_guitars():
    guitars_list = []
    in_file = open('guitars.csv', 'r', newline='')
    for line in in_file:
        words = line.strip().split(",")
        new_guitar = Guitars(words[0], words[1], words[2])
        guitars_list.append(new_guitar)
        guitars_list.sort()
    for i in guitars_list:
        print(i)
    in_file.close()

sort_guitars()
