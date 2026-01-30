gpa = float(input("Enter your gpa (0.0 - 4.0): "))
hours = int(input("Enter number of volunteer hours: "))

if gpa >= 3.5 and hours < 100:
  result = "Scholarship approved!"
elif gpa < 3.5 and hours >= 100:
  result = "Scholarship approved"
else:
  result = "Scholarship denied"

print(result)
