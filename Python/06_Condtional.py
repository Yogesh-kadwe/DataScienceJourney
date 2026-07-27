


# ---------------------------------------------#




# # 1 to 10
# num=int(input("Enter a number : "))
# i=0
# while i<=num-1:
#     i+=1
#     print(i)
    



# 10 to 1

# num=int(input("Enter a number : "))
# i=0
# while i<num:
#     print(num-i)
#     i+=1
    
# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

# EVEN NUMBER

# num=int(input("Enter a number : "))
# i = 2
# while i <= num:
#     print(i)
#     i += 2



# sum of number
# num=int(input("Enter a number : "))
# sum=0
# i = 0
# while i <= num-1:
#     i+=1
#     sum += i
# print("the total sum of this number is : ",sum)

# ---------------------------------------------#


# Write a program to calculate the factorial of a number.
# num=int(input("Enter a number : "))
# fact=1
# i = 0
# while i <num:
#     i+=1
#     fact *= i

# print("the factorial of this number is : ",fact)



# second method
# i = 1
# fact = 1

# while i <= num:
#     fact *= i
#     i += 1


# ---------------------------------------------#

# Write a program to print the multiplication table of any number
# num=int(input("Enter a table number that want to print : "))
# i=1
# while i<=10:
#     print(f"{num} * {i} = {num * i}")
#     i+=1


# ---------------------------------------------#
# Write a program to count how many digits are present in a number.

# num=input("Enter a number : ")
# print(len(num))

# num = int(input("Enter a number: "))

# count = 0

# while num > 0:
#     count += 1
#     num = num // 10

# print("Total digits:", count)
    
# ---------------------------------------------#
# Practice Questions
# Write programs using a for loop.


# # Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i)


# # Print even numbers from 2 to 20.
# for i in range(2,21,2):
#     print(i)


# Print the multiplication table of any number.
# num=int(input("Enter Table number to print : "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# ---------------------------------------------#


# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


# ---------------------------------------------#\

# *****
# ****
# ***
# **
# *

# for i in range(1, 6):
#     for j in range(5, i - 1, -1):
#         print("*", end="")
#     print()



# ---------------------------------------------#
# 1
# 12
# 123
# 1234
# 12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


  # ---------------------------------------------#



# 12345
# 1234
# 123
# 12
# 1

# for i in range(1, 6):
#     for j in range(1,7-i):
#         print(j, end="")
#     print()




    # ---------------------------------------------#

#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")

#     for j in range(1, i + 1):
#         print("*", end="")

#     print()

    # ---------------------------------------------#

#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1, 6):

#     # Print spaces
#     for j in range(1, 6 - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(1, 2 * i):
#         print("*", end="")

#     # Move to the next line
#     print()


    # ---------------------------------------------#


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# Upper Half
for i in range(1, 6):

    for j in range(1, 6 - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print("*", end="")

    print()

# Lower Half
for i in range(4, 0, -1):

    for j in range(1, 6 - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print("*", end="")

    print()
    # ---------------------------------------------#