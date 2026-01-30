message = input("Enter a message: ")
word = input("Enter the word to find in the message: ")

word_to_find = message.find(word)

if word_to_find == -1:
  result = "Not found"
else:
  result = f"Word found at {word_to_find} position"
  
print(result)
