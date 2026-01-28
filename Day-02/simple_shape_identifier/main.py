a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = float(input("Enter side c:"))

if a == b == c:
  print("Equilateral")
elif (a == b and b != c) or (a == c and a != b) or (b == c and a != b):
  print("Isosceles")
else:
  print("Scalene")
