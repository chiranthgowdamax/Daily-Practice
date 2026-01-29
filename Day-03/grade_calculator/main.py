score = int(input("Enter student's score: "))

if score < 0 or score > 100:
  grade = "Invalid Score"
elif score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"

print(grade)
