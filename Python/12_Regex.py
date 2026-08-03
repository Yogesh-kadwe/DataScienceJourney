
          # REGEX#

import re

text="I am learning Python"
if re.search("Python",text):
    print("Found")
else:
    print("Not Found")





text="Python is easy"
if re.match("Python",text):
    print("Matched")
else:
    print("Not Matched")






text="apple mango apple banana apple"
result=re.findall("apple",text)
print(result)



import re
text="I like Java"
result=re.sub("Java","Python",text)
print(result)



text="red,blue,green,yellow"
result=re.split(",",text)
print(result)

