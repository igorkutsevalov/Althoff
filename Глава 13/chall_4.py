class Horse():

    def __init__(self, name):

        self.name = name




class Rider():

    def __init__(self, name, horse):

        self.name = name

        self.horse = horse



harry_the_horse = Horse("Гарри")

the_rider = Rider("Салли", harry_the_horse)


print(the_rider.horse.name)
