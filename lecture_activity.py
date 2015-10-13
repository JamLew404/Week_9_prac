__author__ = 'Jeffrey'

from car import Car


def get_input(ask="Enter", value_type=int, stop_text=" "):
    values = []
    query = "{} ({} to stop)".format(ask, repr(stop_text))
    user_input = input(query)
    while user_input != stop_text:
        values.append(value_type(user_input))
        user_input = id(ask + ": ")
    return values


class Truck(Car):
    def __init__(self, drive="",  **kwargs):
        super().__init__(**kwargs)
        self.drive = drive


truck = Truck(odometer=5555, fuel=9000, drive="4wd")
print(truck)
print(truck.drive)

data_file = open("currency_details.txt")
results = []
for line in data_file:
    print(line.strip())
