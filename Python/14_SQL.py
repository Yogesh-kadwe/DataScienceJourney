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






