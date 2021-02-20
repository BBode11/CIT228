def get_formatted_city(city, country, population=0):
    if population:
        city_info = f"{city}, {country} - population: {population}"
    else:
        city_info = f"{city}, {country}"
    return city_info.title()