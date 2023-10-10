import pandas as pn
import numpy as pi
class Staff:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Teacher(Staff):
    def __init__(self, id, name, subject, publication):
        super().__init__(id, name)
        self.subject = subject
        self.publication = publication

class Typist(Staff):
    def __init__(self, id, name, speed):
        super().__init__(id, name)
        self.speed = speed

class Officer(Staff):
    def __init__(self, id, name, grade):
        super().__init__(id, name)
        self.grade = grade

class Regular(Typist):
    def __init__(self, id, name, speed, salary):
        super().__init__(id, name, speed)
        self.salary = salary

class Casual(Typist):
    def __init__(self, id, name, speed, dailywage):
        super().__init__(id, name, speed)
        self.dailywage = dailywage

def display_menu():
    print("Menu:")
    print("1. Add Regular Typist")
    print("2. Add Casual Typist")
    print("3. Exit")

regular_typists = []
casual_typists = []

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        speed = float(input("Enter Typing Speed: "))
        salary = float(input("Enter Salary: "))
        regular_typists.append(Regular(id, name, speed, salary))
        print("Regular Typist added.")

    elif choice == 2:
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        speed = float(input("Enter Typing Speed: "))
        dailywage = float(input("Enter Daily Wage: "))
        casual_typists.append(Casual(id, name, speed, dailywage))
        print("Casual Typist added.")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

for i in casual_typists:
    print(f"casual_typsit:{i}")
    print(f"ID: {i.id}, Name: {i.name}, Speed: {i.speed}, Daily Wage: {i.dailywage}")
for j in regular_typists:
    print(f"regular_typsit:{j}")
    print(f"ID: {j.id}, Name: {j.name}, Speed: {j.speed}, salary: {j.salary}")