sandwich_orders = ["BLT", "Pastrami", "Club", "Vito", "Pastrami", "Cubano", "PB&J", "Pastrami", "Pulled Pork", "Turkey"]
finished_sandwiches = []

print("\n Oh no! \n We just ran out of pastrami!")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n \tSandwiches that were made today:")
for v in finished_sandwiches:
    print("\t\t", v.title(), "sandwich")