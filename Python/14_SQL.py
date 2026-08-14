# # Customer (cname, street, city)
# # Deposit (cname, accno)
# # Loan (loanno, bname, amt)
# # Borrow (cname, loanno)
# # Write an SQL query to:
# # Find the lowest amount of loan at the bank named AXIS.

# SELECT MIN(amt)
# FROM Loan
# WHERE bname = 'AXIS';





# # Using:
# # Customer (cname, street, city)
# # Deposit (cname, accno)
# # Loan (loanno, bname, amt)
# # Borrow (cname, loanno)
# # Write a query to:
# # Find all customer names having a loan amount greater than 50,000.

# SELECT cname
# FROM Borrow;






# # Schema:

# # Customer (cname, street, city)
# # Deposit (cname, accno)
# # Loan (loanno, bname, amt)
# # Borrow (cname, loanno)
# # Find all customer names having either an account or a loan or both.

# SELECT cname
# FROM Deposit

# UNION

# SELECT cname
# FROM Borrow;


















# Customer (cname, street, city)
# Deposit (cname, accno)
# Loan (loanno, bname, amt)
# Borrow (cname, loanno)
# Find names of customers having either an account or a loan or both.












# # Find all city names containing the character n.
# SELECT city
# FROM Customer
# WHERE city LIKE '%n%';




# # Find all branch names whose names are not ending with a.

# SELECT bname
# FROM Loan
# WHERE bname NOT LIKE '%a';








# # What are string functions?

# String functions are SQL functions used to perform operations 
# on character or text data, such as changing case, finding length, 
# joining strings, and extracting portions of strings