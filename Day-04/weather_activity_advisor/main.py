temperature = int(input("Enter temperature: "))
is_raining = input("Is it raining? (yes/no): ")

if 15 <= temperature <= 25 and not (is_raining == "yes"):
  result = "Go for a walk!"
else:
  result = "Stay inside!"

print(result)
