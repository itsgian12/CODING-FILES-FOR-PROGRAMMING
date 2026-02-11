class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def oldest_cat(*cats):
        return max(cats, key=lambda cat: cat.age) 

x = Cat("bob", 5)
y = Cat("sam", 8)
z = Cat("gray", 10) 

oldest = oldest_cat(x,y,z)


print(f'Oldest cat is {oldest.name}, {oldest.age}years old')
# WRONG CODE FOR OLDEST NAME, FIX LATER