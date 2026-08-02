# # Program 1
# # Create a class named:
# # Student
# # Create two objects:
# # student1
# # student2
# # Print both objects.

# class student():
#     pass

# student1=student()
# student2=student()
# print(student1)
# print(student2)


# # Program 2
# # Create a class:
# # Car
# # Create three objects:
# # car1
# # car2
# # car3
# # Print all three.
# class Car:
#     pass
# car1 = Car()
# car2 = Car()
# car3 = Car()
# print(car1)
# print(car2)
# print(car3)



# class Mobile:
#     pass

# mobile1 = Mobile()
# mobile2 = Mobile()

# print(type(mobile1))
# print(type(mobile2))

# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
# Student1=Student("Yogesh",20)
# print(Student1.name)
# print(Student1.age)



# class Car():
#     def __init__(self,brand,model):
#         self.brand= brand
#         self.model= model
# car1=Car("Toyata","Fortuner")
# print(car1.brand)
# print(car1.model)



# class Employee():
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
# e1=Employee("Rahul",50000)
# e2=Employee("Amit",70000)
# print(e1.name , e1.salary)
# print(e2.name , e2.salary)


# class Student:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, I am {self.name}")

# s1 = Student("Yogesh")
# s1.greet()







# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         print("Addition:", self.num1 + self.num2)

# c1 = Calculator(20, 30)
# c1.add()





# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area:", self.length * self.width)

# r1 = Rectangle(20, 13)
# r1.area()




# class Student():
#     def __init__(self,name):
#         self.__name=name
#     def show_name(self):
#         print(f"Name : {self.__name}")

# s1=Student("Yogesh")
# s1.show_name()



# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         return self.__balance


# account = BankAccount(5000)

# account.deposit(2000)

# print("Balance:", account.show_balance())









# class Employee():
#     def __init__(self):
#         self.__salary="50000"
#     def show_salary(self):
#         return self.__salary


# emp=Employee()
# print(emp.show_salary())








# class Employee:

#     def __init__(self):
#         self.__salary = 50000

#     def set_salary(self, salary):

#         if salary > 0:
#             self.__salary = salary

#         else:
#             print("Invalid Salary")

#     def show_salary(self):
#         return self.__salary


# emp = Employee()

# emp.set_salary(400000)

# print(emp.show_salary())





# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def show_balance(self):
#         return self.__balance


# account = BankAccount(5000)

# account.withdraw(2000)

# print("Balance:", account.show_balance())






# class Person:
#     def show_name(self):
#         print("Name : Yogesh")

# class Student(Person):
#     def study(self):
#         print("Studying Python")

# obj=Student()
# obj.show_name()
# obj.study()







# class Father:
#     def money(self):
#         print("Money is avalilable")

# class Mother(Father):
#     def care(self):
#         print("mother care for child")

# class Child(Mother):
#     print("child class")

# obj=Child()
# obj.money()
# obj.care()




# class Animal:
#     def eat(self):
#         print("Lion eats apple")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Puppy(Animal):
#     def play(self):
#         print("Puppy is Playing")

# obj=Puppy()
# obj2=Dog()
# obj.eat()
# obj2.bark()
# obj.play()








# class Person:
#     def __init__(self):
#         print("Person Constructor")

# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         print("Student Cnstructor")

# obj=Student()







# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def eat(self):
#         super().eat()
#         print("Dog is eating")

# obj=Dog()
# obj.eat()


# class Person:

#     def __init__(self, name):
#         self.name = name


# class Student(Person):

#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course

#     def show(self):
#         print("Name :", self.name)
#         print("Course :", self.course)


# obj = Student("Yogesh", "Data Science")

# obj.show()




# # Method Overriding
# class Vehicle:

#     def start(self):
#         print("Vehicle Started")


# class Car(Vehicle):

#     def start(self):
#         print("Car Started")


# obj = Car()

# obj.start()


# class Employee:

#     def work(self):
#         print("Employee Working")


# class Developer(Employee):

#     def work(self):
#         print("Developer Writing Code")


# obj = Developer()

# obj.work()


# class Animal:
#     def eat(self):
#         print("Animal Eating")

# class Dog(Animal):
#     def eat(self):
#         super().eat()
#         print("Dog Eating")

# obj=Dog()
# obj.eat()




# Polymorphism  #

# class Animal:
#     def sound(self):
#         print("Animal")

# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat Meows")

# obj1=Cat()
# obj=Dog()
# obj.sound()
# obj1.sound()




# class Shape:
#     def draw(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("Drawing Circle")

# class Rectangle(Shape):
#     def draw(self):
#         print("Drawing Rectangle")

# def draw_shape(shape):
#     shape.draw()

# obj1 = Circle()
# obj2 = Rectangle()

# draw_shape(obj1)
# draw_shape(obj2)




# class Vehicle:
#      pass

# class Car(Vehicle):
#      def move(self):
#           print("Car is Moving")

# class Bike(Vehicle):
#      def move(self):
#           print("Bike is Moving")

# obj = Car()
# obj2 = Bike()

# obj.move()
# obj2.move()



# # Class and Instance Variable

# class Student:
#     college="SBJITMR"

#     def __init__(self):
#         self.name="Yogesh"
        

# s1=Student()
# s2=Student()
# s2.name="Rahul"
# print(s1.name,s1.college)
# print(s2.name,s2.college)





# class Employee:
#     company="Google"
#     def __init__(self):
#         self.name="Amit"

# e1=Employee()
# e2=Employee()
# e2.name="Priya"
# print(e1.name)
# print(e2.name)






# class Car:
#     wheels = 4
#     def __init__(self):
#         self.brand="Toyata"

# c1=Car()
# c2=Car()
# c2.brand="BMW"
# print(c1.brand,c1.wheels)
# print(c2.brand,c2.wheels)











# Topic: Instance Method vs @classmethod vs @staticmethod



class Student:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print(self.name)

obj=Student("Yogesh")
obj.show_name()





class Student:
    college="SBJITMR"
    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()



class Calculator:
    @staticmethod
    def multiiply(a,b):
        print(a*b)

Calculator.multiiply(45,54)