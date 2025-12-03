# Single inheritance 
class Person: 
    def __init__(self, name): 
        self.name = name 
 
class Student(Person): 
    def __init__(self, name, roll): 
        super().__init__(name) 
        self.roll = roll 
 
    def display(self): 
        print(f"Name: {self.name}, Roll: {self.roll}") 
 
s = Student("Charlie", 103) 
s.display() 
 
# Method overriding example 
class Animal: 
    def sound(self): 
        print("Animal sound") 
 
class Dog(Animal): 
    def sound(self): 
        print("Bark") 
 
dog = Dog() 
dog.sound() 
 
# Abstract class example 
from abc import ABC, abstractmethod 
 
class Shape(ABC): 
    @abstractmethod 
    def area(self): 
        pass 
 
class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
 
    def area(self): 
        return self.width * self.height 
 
rect = Rectangle(5, 3) 
print("Area of rectangle:", rect.area())
