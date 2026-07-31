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


# class Student():
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         print("Hello, I am Yogesh")

# s1=Student("Yogesh")
# s1.greet()



class Calculator():
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        num3=num1+num2
        print("Addition : ",num3)

c1=Calculator()
c1.add(20,30)


class Rectangle():
    def area(self,length,width):
        self.length=length
        self.width=width
        print("Area of Rectangle : ",length*width)

r1=Rectangle()
r1.area(20,13)