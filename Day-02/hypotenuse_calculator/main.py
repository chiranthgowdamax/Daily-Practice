import math

base = float(input("Enter the base: "))
perpendicular = float(input("Enter the perpendicular: "))

hypotensuse = math.sqrt(base**2 +perpendicular**2)

print(f"Base: {base}")
print(f"Perpendicular: {perpendicular}")
print(f"Hypotensuse: {round(hypotensuse, 2)}cm²")
