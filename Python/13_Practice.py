
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




# # Easy method prime number
# for num in range(2, 101):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")




# # Write a program to reverse a string without using slicing ([::-1]).
# text=input("Enter a string : ")
# rev=""
# for ch in text:
#     rev=ch+rev
# print(rev)


# # Count the Number of Vowels
# text=input("Enter the String : ")
# count=0
# for i in text:
#     if i in "AEIOUaeiou":
#         count+=1
# print(count)
    



# text = input("Enter String: ").lower()
# count = 0
# for ch in text:
#     if ch in "aeiou":
#         count += 1

# print(count)







# # Write a program to remove duplicate elements from a list without using set().
# list=[10, 20, 10, 30, 20]
# unique_list=[]
# for i in list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)







# # Write a program to find the largest element in a list without using the built-in max() function.
# numbers = [45, 12, 89, 34, 67]
# large=numbers[0]
# for i in numbers:
#     if i>large:
#         large=i
# print(large)




text = input("Enter String: ").lower()

frequency = {}
for ch in text:
    if ch in frequency:
     print(ch)
    else:
        print(ch)

