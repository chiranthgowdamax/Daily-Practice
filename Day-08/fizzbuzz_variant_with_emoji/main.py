num = int(input("Enter an integer ≥ 1 or ≤ 20: "))

if 1 <= num <= 20:
  for x in range(1, num+1):
    if x % 3 == 0 and x % 5 == 0:
      print(f"{x}✨⭐")
    elif x % 3 == 0:
      print(f"{x}✨")
    elif x % 5 == 0:
      print(f"{x}⭐")
    else:
      print(x)
