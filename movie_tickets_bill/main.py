movie_name = input("Enter movie name: ")
ticket_price = float(input("Enter ticket price: "))
no_of_tickets = int(input("Enter the number of tickets: "))

total_cost = ticket_price * no_of_tickets

print(f"Movie: {movie_name}")
print(f"Total cost is ₹{total_cost:.2f}")
