pocket_money = float(input("Enter pocket money: ₹"))
money_spent_on_snacks = float(input("Enter money spent on snacks: ₹"))
money_spent_on_travel = float(input("Enter money spent on travel: ₹"))

pocket_money -= money_spent_on_travel + money_spent_on_snacks
remaining_money = pocket_money

print(f"Remaining money: ₹{remaining_money}")
