'''
In Python, classes and objects are fundamental concepts of Object-Oriented Programming (OOP).

Classes:
A class acts as a blueprint or a template for creating objects. It defines the structure and behavior that objects of that class will possess. Classes are defined using the class keyword.This includes:
Attributes: Variables that store data associated with an object. These define the characteristics or properties of an object.
Methods: Functions defined within a class that describe the actions or behaviors an object can perform.

Objects:
An object is an instance of a class. It is a concrete entity created from the blueprint defined by the class. Each object has its own unique set of attribute values and can execute the methods defined in its class.
Objects are created by calling the class as if it were a function:


Relationship Between Class and Objects :
A class defines what an object will be like, while an object is a specific realization of that definition.
You can create multiple objects from a single class, each with its own distinct data but sharing the same methods and overall structure.

'''


class Dog:    # Blueprint/Template  - Custom Class

    # variables -> Class attributes
    def __init__(self, dog_name, dog_age, dog_breed, dog_color):
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed
        self.color = dog_color

    # function -> Class methods
    def bark(self):    # self Object/Instances creating
        print(f"{self.name} Woof Woof" )

    def display_Dog_Info(self):
        print(f"Dog Info- "
              f" Name: {self.name}"
              f" Age: {self.age}"
              f" Breed: {self.breed}"
              f" Color: {self.color}")

# Use the Dog Class
murphy = Dog("Murphy", 5, "Cannis", "Brown")      # Object = Class()
murphy.bark()
murphy.display_Dog_Info()


denis = Dog("Dennis", 3, "Cannis", 3)
denis.bark()
denis.display_Dog_Info()





# Use Random Class
import random        # Predefined Class - Random

num = random.Random()