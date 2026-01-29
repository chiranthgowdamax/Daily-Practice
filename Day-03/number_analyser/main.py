num = int(input("Enter a number: "))

if num > 0:
  sign = "Positive"
elif num < 0:
  sign = "Negative"
else:
  sign = "Zero"
  
if num % 2 == 0:
  parity = "Even"
else:
  parity = "Odd"

abs_num = abs(num)

if abs_num < 10:
  digits = "Single-digit"
elif abs_num < 100:
  digits = "Double-digit"
elif abs_num < 1000:
  digits = "Triple-digit"
else:
  digits = "Multi-digit"
  
print(f"{sign}, {parity}, {digits}")
