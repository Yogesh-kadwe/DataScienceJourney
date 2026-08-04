
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








import re
text="I Love Data Science"
if re.findall(r"Science$",text):
    print("Starts with Python")
else:
    print("Not Started with Python")