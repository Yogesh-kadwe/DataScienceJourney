

# def Hello():
#     print("Welcome to Python")

# Hello()
# Hello()
# Hello()


# def student():
#     name = "Yogesh"
#     course = "Data Science"
#     college = "S.B Jain Institute of Technology Nagpur"

#     print("Name:", name)
#     print("Course:", course)
#     print("College:", college)

# student()


# def calculator():
#     print("10 + 20 =", 10 + 20)
#     print("10 * 20 =", 10 * 20)

# calculator()



# def greet(name):
#     print("Hello",name)
# greet("Yogesh")

# def add(num1,num2):
#     print("Addition : ",num1+num2)
# add(10,20)


# def student(name,course):
#     print("Name : ",name)
#     print("Course : ",course)
# student("Yogesh","Data Science")




# def square(num):
#     return num*num

# sq=square(5)
# print(sq)




# def cube(num):
#     return num*num*num

# result=cube(5)
# print(result)




# def largest(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# result=largest(10,25)
# print(result)



 # ---------------------------------------------#

            # LAMBDA FUNCTION

 # ---------------------------------------------#

# add = lambda a,b: a+b
# print(add(15,25))


# square =lambda x:x*x
# print(square(9))

# largest = lambda a,b:a if a>b else b
# print(largest(40,25))


 # ---------------------------------------------#
       # MAP FUNCTION

# Program 1
# Double every number in the list.

# numbers= [2,4,6,8]
# result=list(map(lambda x:10+x,numbers))
# print(result)





# Program 2
# Find the square of every number

# numbers=[1,2,3,4,5,6]
# result=list(map(lambda x:x*x,numbers))
# print(result)






# Program 3
# Convert every name to uppercase.

# names = ["yogesh", "rahul", "amit"]
# result=list(map(lambda x:len(x),names))
# print(result)
  # ------------------
  # FILTER FUNCTION 

# Keep only odd numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7]

# result = list(filter(lambda x: x % 2 != 0, numbers))

# print(result)



# # Keep numbers greater than 50.
# numbers = [10, 45, 60, 70, 20, 90]
# result=list(filter(lambda x:x>50,numbers))
# print(result)

# # Keep names with more than 5 characters.
# names = ["Ram", "Yogesh", "Rahul", "Amit", "Prakash"]
# result=list(filter(lambda x:len(x)>5,names))
# print(result)


  # ----------------------------------------------#

        # REDUCE() FUNCTION

# # Find the sum of all numbers.
# from functools import reduce
# numbers = [10, 20, 30, 40]
# result=reduce(lambda a,b :a+b ,numbers)
# print(result)


# # Find the product of all numbers.
# from functools import reduce
# numbers = [2, 3, 5]
# result=reduce(lambda a,b:a*b,numbers)
# print(result)


# # Find the smallest number.
# from functools import reduce
# numbers = [45, 10, 80, 25]
# result=reduce(lambda a,b: a if a<b else b,numbers)
# print(result)

from functools import reduce
numbers = [25, 80, 15, 90, 60]
result=reduce(lambda a,b:a if a>b else b,numbers)
print(result)

   # ---------------------------------------------#




    # ---------------------------------------------#





     # ---------------------------------------------#