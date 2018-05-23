# import sys
# print sys.version_info

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print("Health: " + str(self.health))
        return self

bunny = Animal("Bunny", 10)
bunny.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)
    def pet(self):
        self.health += 5
        return self

dog = Dog("winston")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name, health=170):
        super().__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon!")

animal2 = Animal("Cat", 100)
#animal2.fly()
#animal2.pet()
animal2.displayHealth()
dragon1 = Dragon("Dragon")
dragon1.displayHealth()
