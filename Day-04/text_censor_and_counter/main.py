message = input("Enter a message: ")

replace = message.replace("bad", "***")

count = message.count("bad")

print(replace)
print(f"Found {count} bad words")
