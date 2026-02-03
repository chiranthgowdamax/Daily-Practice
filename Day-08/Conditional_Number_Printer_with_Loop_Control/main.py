start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for x in range(start, end+1):
  if x > 50:
    break
  elif x % 3 == 0:
    continue
  print(x)
