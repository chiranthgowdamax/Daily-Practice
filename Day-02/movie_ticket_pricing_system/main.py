age = int(input("Enter your age: "))
time = int(input("Enter time in 24-hour format and in round figure: "))
day_type = input("Daytype (weekend/weekday): ")
price = 10


if age < 12:
  price = price * 0.70
elif 12 <= age <= 17:
  price = price * 0.80
elif age >= 65:
  price = price * 0.75

  
if time < 12:
  price = price - 2


if day_type == "weekend":
  price = price * 1.15


print(f"Final price: ${round(price, 2)}")
