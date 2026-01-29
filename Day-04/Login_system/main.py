username = input("Enter the username: ")
password = input("Enter the password: ")


if username == "admin" and password == "1234":
  result = "Access granted"
else:
  result = "Access denied"
  
print(result)
