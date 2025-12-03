class Student: 
    def __init__(self, name, roll): 
        self.name = name 
        self.roll = roll 
 
    def display(self): 
        print(f"Name: {self.name}, Roll: {self.roll}") 
 
    def update_roll(self, new_roll): 
        self.roll = new_roll 
 
s = Student("Bob", 102) 
s.display() 
s.update_roll(105) 
s.display()
