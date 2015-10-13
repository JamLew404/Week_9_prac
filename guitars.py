__author__ = 'Jeffrey'


class GuitarError(Exception):
    def __init__(self, value):
        super().__init__(value)


class Guitars:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        if year < 0:
            raise GuitarError("Age cannot be less than 0!")


    def get_age(self):
        current_year = 2015
        age_of_guitar = current_year - int(self.year)
        return age_of_guitar

    def is_vintage(self):
        current_year = 2015
        age_of_guitar = current_year - int(self.year)
        if age_of_guitar > 50:
            return True
        else:
            return False

    def __str__(self):
        return ' " {:>20} was made in {:>6} and is worth ${:10.2f}" '.format(self.name, self.year,self.cost)


boo = Guitars("bob", -9, 123)