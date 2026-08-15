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











# # employee (Eid, Ename, street, city, Sal)
# # Find all employees who live in the city Nagpur.

# select *
# from employee
# where city in ('Nagpur');







# # Find all customer names whose balance is between 10,000 and 20,000 at bank SBI.
# # Customer (cid, cname, city, age)
# # Account (accno, bid, bal)
# # Depositor (cid, accno, cname)
# # Loan (loanno, bid, lamt)
# # Borrower (cid, loanno, cname)
# # Branch (bid, bname, city)

# SELECT D.cname
# FROM Depositor D
# JOIN Account A
#     ON D.accno = A.accno
# JOIN Branch B
#     ON A.bid = B.bid
# WHERE A.bal BETWEEN 10000 AND 20000
#   AND B.bname = 'SBI';






# # Find the second largest amount of balance.
# SELECT bal
# FROM Account
# ORDER BY bal DESC
# LIMIT 1 OFFSET 1;


# Find the total loan amount given by SBI.
# Loan (loanno, bid, lamt)
# Branch (bid, bname, city)

select sum(lamt)
from Loans


