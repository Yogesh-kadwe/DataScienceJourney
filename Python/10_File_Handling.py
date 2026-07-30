# # Program 1
# # Read and print the contents of student.txt

# file=open("student.txt","r")
# print(file.read())
# file.close()


# # Program 2
# # Write the following into student.txt:
# file=open("student.txt","w")
# file.write("Python \n Data Science")
# file.close()


# # Program 3
# # Append the following line to the same file:
# file=open("student.txt","a")
# file.write("Machine Learning")
# file.close()


# # Program 1
# # Create a file named fruits.txt with:
# # Aple
# # Banana
# # Mango
# # Orange
# with open("fruits.txt","r") as file:
#     print(file.readline())



# Program 2
# Create a file named students.txt with the following content:
# Yogesh
# Rahul
# Amit
# Priya
# Sneha

# with open("fruits.txt","r") as file:
#     lines=file.readlines()
#     for line in lines:
#          print(line.strip())


# Program 3
# Using the same students.txt file, write a program that:
# Opens the file using with open()
# Reads all the lines
# Counts how many students are in the file
# Prints:
# Total Students: 5

# with open("students.txt", "r") as file:
#     lines = file.readlines()

# print("Total Students:", len(lines))

with open("students.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        print(f"Student {len(line)} :", i)