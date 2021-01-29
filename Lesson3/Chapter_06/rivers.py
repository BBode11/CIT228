rivers={
	"Zambezi": ["Zambia", "Angola", "Namibia", "Botswanna", "Zimbabwe", "Mozambique"],
	"Mississippi": "United States",
	"Mekong": ["China", "Burma", "Laos", "Thailand", "Cambodia", "Vietnam"],
	}

print("-------------------- Rivers and Countries ----------------------\n")
for key, value in rivers.items():
	print(f"The {key.title()} river flows through {value} \n")

print("-------------------- Rivers -------------------\n")
for key in rivers.keys():
	print(key.title())

print("-------------------- Countries -------------------\n")
for value in rivers.values():
	print(value , "\n")