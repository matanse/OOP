class Human(object):
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hey {self.name}, welcome!')


class Woman(Human):
    pass


class Man(Human):
    def __init__(self, name, gender):
        super(Man, self).__init__(name)
        self.gender = gender

    def cheat(self, gender):
        print(f'some {self.gender} cheat on {gender}! ')


class Hanna(Woman):
    def eating(self):
        print(f'I am eating and my name is {self.name}')

    def show_hair(self):
        print(f'my hair is {self.hair}')


class Mati(Man):
    def greeting(self):
        print(f'Hey thats {self.name} and he is a {self.gender}')


class Baby(Mati, Hanna):
    pass


hanna = Hanna('Hanna')
hanna.hair = "braun"
hanna.eyes = "green"
hanna.height = 167


mati = Mati('Mati', 'Men')

# print("hanna has: ")
# print(hanna.hair + " hair " + hanna.eyes + " eyes " +
#       "she is " + str(hanna.height) + " tall")


hanna.greeting()
hanna.eating()
hanna.show_hair()
print('')
print('')
print('')
mati.greeting()
mati.cheat('woman')

mati.
