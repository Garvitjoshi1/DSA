class Person(object):  # Parent class
    def __init__(self, name, id_card):
        self.name = name
        self.id_card = id_card

    def display(self):
        print(self.name, self.id_card)


# Inherited or child class made out of parent class
class Emp(Person):
    def Print(self):
        print("Emp class called")


Emp_details = Emp("Mayank", 103)  # details entered in inherited class
Emp_details.display()  # display function used
Emp_details.Print()  # Print function used
emp = Person("Satyam", 102)
# new object emp created to store value in class Person
emp.display()
