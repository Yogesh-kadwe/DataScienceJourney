
name=input("Enter Name : ")
Roll_number=int(input("Enter Roll Number : "))
python_marks=float(input("Enter Python marks obtained : "))
sql_marks=float(input("Enter SQL marks obtained : "))
math_marks=float(input("Enter Mathematics  marks obtained : "))
print("------Student Report Card-------")
print("Name : ",name)
print("Roll Number : ",Roll_number)
print("\n")
print("Python : ",python_marks)
print("SQL : ",sql_marks)
print("Mathematics : ",math_marks)
print("\n")
total=python_marks+sql_marks+math_marks
avarage=total/3
print("Total : ",total)
print("Average : ",average)