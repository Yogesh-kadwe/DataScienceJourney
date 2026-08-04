
          # REGEX#

# import re

# text="I am learning Python"
# if re.search("Python",text):
#     print("Found")
# else:
#     print("Not Found")





# text="Python is easy"
# if re.match("Python",text):
#     print("Matched")
# else:
#     print("Not Matched")






# text="apple mango apple banana apple"
# result=re.findall("apple",text)
# print(result)



# import re
# text="I like Java"
# result=re.sub("Java","Python",text)
# print(result)



# text="red,blue,green,yellow"
# result=re.split(",",text)
# print(result)







# # SPECIAL METHOD
# | Pattern | Meaning                   |
# | ------- | ------------------------- |
# | `\d`    | Digit                     |
# | `\D`    | Not a digit               |
# | `\w`    | Letter, digit, underscore |
# | `\W`    | Special character         |
# | `\s`    | Space                     |
# | `\S`    | Not a space               |
# | `^`     | Start of string           |
# | `$`     | End of string             |
# | `+`     | One or more               |
# | `*`     | Zero or more              |
# | `?`     | Zero or one               |






# import re

# text = "Python123Data45"

# print(re.findall(r"\d", text))








# import re

# text = "Python@123#AI!"

# print(re.findall(r"\W", text))







# import re

# text = "I Love Data Science"

# print(re.findall(r"\s", text))





# import re
# text="Python is awesome"
# if re.findall(r"^Python",text):
#     print("Starts with Python")
# else:
#     print("Not Started with Python")






# 🎤 Most Asked Interview Questions
# Q1. What does \d represent?
# ✅ Ready Interview Answer

# "\d matches any single digit from 0 to 9."

# Q2. Why do we write r"..." in Regex?
# ✅ Ready Interview Answer

# "The r creates a raw string, preventing 
# Python from interpreting backslashes as escape characters. 
# This makes regex patterns more reliable and readable."

# Q3. What does ^ do?
# ✅ Ready Interview Answer

# "^ matches the beginning of a string."

# Q4. What does $ do?
# ✅ Ready Interview Answer

# "$ matches the end of a string."











# import re
# text="I Love Data Science"
# if re.findall(r"Science$",text):
#     print("Ends with Science")
# else:
#     print("Not Ends with Science")







# # 1️⃣ Email Validation
# # Check whether an email is valid.
# import re

# email = input("Enter Email: ")

# pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")




# 2️⃣ Mobile Number Validation
# Assume a valid mobile number has exactly 10 digits.
import re

mobile = input("Enter Mobile Number: ")

pattern = r"^\d{10}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")