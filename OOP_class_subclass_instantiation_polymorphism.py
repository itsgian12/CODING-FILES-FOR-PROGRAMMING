class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())\

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Sylvester(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
    
# my_cats = []
# cat1 = Simon('Simon', 10)
# cat2 = Sally('Sally', 15)
# cat3 = Sylvester('Sylvester', 5)

# my_cats.append(cat1)
# my_cats.append(cat2)
# my_cats.append(cat3)
# /////////////this is all same as on the bottom

my_cats = [Simon('Simon', 10), Sally('Sally', 15), Sylvester('Sylvester', 5)]

my_pets = Pets(my_cats)

my_pets.walk()