battery = int(input("Enter battery percentage: "))

if battery < 0 or battery > 100:
  print("Not valid")
elif battery >= 0 and battery <= 20:
  print("Critical! Charge Now.")
elif battery >= 21 and battery <= 50:
  print("Low battery. Save power.")
elif battery >= 51 and battery <= 80:
  print("Battery is okay.")
else:
  print("Battery full. Unplug charger")
