email = input("Enter gmail with '@' included: ")

position = email.find("@")
username = email[0:position]

print(f"Username: {username}")
