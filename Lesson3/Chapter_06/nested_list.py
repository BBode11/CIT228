baseballTeams={
    "Michigan": ["Detroit Tigers", "Lansing Lugnuts", "West Michigan Whitecaps", "Great Lakes Loons"],
    "Florida": ["Florida Marlins", "Tampa Bay Devil Rays", "Pensacola Blue Wahoos", "Jacksonville Jumbo Shrimp", "Daytona Tortugas", "Bradenton Marauders"]
    }

for key, value in baseballTeams.items():
    if type(value) == list:
         print(f"{key.title()} baseball teams: ")
         for v in value:
            print("\t\t\t\t",v)
    else:    
        print(f"{key.title()} baseball teams {value.title()}")