password = input("Enter a strong password: ")

if len(password) < 8:
  result = "Too short"
else:
  result = "Password accepted"
  
print(result)
