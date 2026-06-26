import random


class Hat:
    houses = ["Gryffindor", "Ravenclaw", "Rufflepuff", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
