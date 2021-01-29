baseballCards={
    "C1":{
        "Name": "Honus Wagner",
        "Year": "1909",
        "Condition": "Excellent",
        "Price": "$3.12 million",
        },

     "C2":{
        "Name": "Mickey Mantle",
        "Year": "1952",
        "Condition": "Excellent",
        "Price": "$2.88 million",
        },

      "C3":{
        "Name": "Bowman Mickey Mantle",
        "Year": "1951",
        "Condition": "Excellent",
        "Price": "$750,000",
        }
    }

for card, info in baseballCards.items():
    print(f"\nBaseball Card: {info['Name']}")
    year = info['Year']
    condition = info['Condition']
    price = info['Price']

    print(f"\tYear: {year}")
    print(f"\tCondition: {condition}")
    print(f"\tPrice: {price}")