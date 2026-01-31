word = input("Enter a word: ").lower()
first_letter = word[0]
last_letter = word[-1]

if first_letter == last_letter:
  result = "Same!"
else:
  result = "Different!"

print(result)
