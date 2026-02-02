username = input("Enter username: ")

while len(username) == 0 or len(username) > 15:
  username = input("Enter username: ")
print("Username accepted")
