
# # EVEN OR ODD
# num = int(input("Enter a Number: "))

# if num % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")



# # Positive Negetive and Zero
# num=int(input("Enter a Number : "))
# if num>0:
#     print(f"{num} is Positive")

# elif num<0:
#     print(f"{num} is Negative")

# else:
#     print(f"{num} is Zero")


# # Largest of Three Numbers
# num1=int(input("Enter a Number 1: "))
# num2=int(input("Enter a Number 2: "))
# num3=int(input("Enter a Number 3: "))

# if num1 >= num2 and num1 >= num3:
#     print(f"The largest number is {num1}")

# elif num2>=num1 and num2>=num3:
#     print(f"The largest number is {num2}")

# else:
#     print(f"The largest number is {num3}")



# # Grade Calculator
# marks=float(input("Enter marks : "))
# if marks < 0 or marks > 100:
#     print("Invalid Marks")
# elif marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# elif marks>=70:
#     print("Grade C")
# elif marks>=60:
#     print("Grade D")
# else:
#     print("Fail")

# # Leap Year Checker
# year=int(input("Enter Year to check if it Leap or Not: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is Not a Leap Year")



# # ATM Withdrawal
# account_balance = float(input("Enter Account Balance: "))
# withdraw_amount = float(input("Enter Withdrawal Amount: "))

# if withdraw_amount > account_balance:
#     print("Insufficient Balance")
# else:
#     account_balance -= withdraw_amount
#     print(f"Remaining Balance: ₹{account_balance}")



# # Suppose the interviewer asks:

# Why did you use if instead of elif?

# The answer is:

# "Because there are only two possible outcomes. 
# Either the withdrawal amount is greater than the balance, or it is not.
#  Since there are only two conditions, if-else is sufficient."


# # BMI Calculator
# weight=float(input("Enter Weight in kg : "))
# height=float(input("Enter Height in m : "))
# bmi=weight/(height**2)
# print(f"Your BMI is: {bmi:.2f}")
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")





# # Simple Calculator

# num1=int(input("Enter First Number : "))
# operator=input("Enter Operator : ")
# num2=int(input("Enter Second Number : "))
# if operator == "+":
#     print(num1+num2)
# elif operator == "-":
#     print(num1-num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     if num2==0:
#         print("Cannot divide by zero")
#     else:
#         print(num1/num2)
# else:
#     print("Invalid Operator")





# Login System

# if username == "admin":
#     if password == "python123":
#         print("Login Successful")
#     else:
#         print("Incorrect Password")
# else:
#     print("User Not Found")



# # Electricity Bill Calculator

# unit=float(input("Enter Units Consumed : "))
# print("Units : ",unit)
# if unit<=100:
#     print("Bill : ",unit*5)

# elif 100< unit <=200:
#     print("Bill : ",unit*7)

# else:
#     print("Bill : ",unit*10)



# ---------------------------------------------#

# if unit <= 100:
#     bill = unit * 5
# elif unit <= 200:
#     bill = unit * 7
# else:
#     bill = unit * 10

# print(f"Total Bill: ₹{bill}")



# ---------------------------------------------#


# Write a Python program to swap two variables
# a=5
# b=7
# print(f"Before Swaping a= {a} and b= {b}")
# temp=a
# a=b
# b=temp
# print(f"After Swaping a= {a} and b= {b}")


# Create a program to count the number of vowels in a string.


# string = input("Enter a string: ")

# count = 0

# for character in string:
#     if character in "aeiouAEIOU":
#         count += 1

# print("Total vowels:", count)


# Write a Python script to reverse a given string.


# str=input("Enter a message : ")
# print(str[::-1])







# # Q10. Check if a number is a palindrome. 

# number = input("Enter a number: ")

# reverse = number[::-1]

# if number == reverse:
#     print("This number is Palindrome.")
# else:
#     print("This number is not Palindrome.")









# Q11. Write a program to find the sum of first N natural numbers. 

















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
num=int(input("Enter a table number that want to print : "))
i=1
while i<=10:
    print(f"{num} * {i} = ",i*num)
    i+=1


# ---------------------------------------------#





# ---------------------------------------------#





# ---------------------------------------------#







# ---------------------------------------------#