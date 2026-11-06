class Person:

    def __init__(self, person_name):
        self.name = person_name

    def message(self):
        print("Hello, ", self.name)


shravya = Person("Shravya Gupta")

shravya.message()

class Dog:
    def __init__(self, name):
        self.name = name 
    def walk(self):
        print(f"{self.name} wants to walk")

class Cat:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f"{self.name} wants to walk")

dog = Dog("Bob")
dog.walk()

cat = Cat("Butter")
cat.walk()
