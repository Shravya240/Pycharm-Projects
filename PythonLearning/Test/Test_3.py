class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


a = Animal()
a.sound()

d = Dog()
d.sound()


class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


b = Bird()
p = Penguin()

b.fly()
p.fly()