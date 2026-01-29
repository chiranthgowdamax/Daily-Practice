weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
if height <= 0:
  print("Invalid height")
else: 
  bmi = weight / (height ** 2)
  
  if bmi < 18.5:
    category = "Underweight"
  elif bmi <= 24.9:
    category = "Normal weight"
  elif bmi <= 29.9:
    category = "Overweight"
  else:
    category = "Obese"
  
  print(f"BMI: {round(bmi, 1)}, Category: {category}")
