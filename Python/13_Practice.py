
# # Q1. Write a Python program to swap two variables.

# a=10
# b=30
# print(f"Before Swapping : A = {a}    B={b}")
# temp=a
# a=b
# b=temp
# print(f"After Swapping : A = {a}    B={b}")




# # Write a program to check if a number is even or odd. 
# num=int(input("Enter the Number : "))
# if num%2==0:
#     print("The Number is Even")
# else:
#     print("The Number is Odd")


# # Create a program that prints the multiplication table of a given number. 
# num=int(input("Enter the table number to print : "))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")





# # Write a program to find the largest of three numbers. 
# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# num3=int(input("Enter third number :"))
# if num1>num2 and num1>num3:
#     print(f"{num1} is largest among three")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is largest among three")
# else:
#     print(f"{num3} is largest among three")






# # Write a program to calculate the factorial of a number.
# num=int(input("Enter a number : "))
# fact=1
# i = 0
# while i <num:
#     i+=1
#     fact *= i

# print("the factorial of this number is : ",fact)



# # Check if a number is a palindrome
# num=input("Enter a Number: ")
# reverse=num[::-1]
# if num==reverse:
#     print("Number is Pallindrome")
# else:
#     print("Number is not Pallindrome")




# #  Write a program to find the sum of first N natural numbers.
# n=int(input("Enter a Number : "))
# sum=0
# for i in range(0,n+1):
#     sum+=i
# print("Sum :",sum)







# #  Write a program to print all prime numbers between 1 and 100. 
# for num in range(2, 101):
#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, end=" ")




# Easy method prime number
for num in range(2, 101):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")