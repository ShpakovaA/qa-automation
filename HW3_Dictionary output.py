# Dictionary output

countries = ["Ukraine", "Spain", "Italy"]

countries_capitals = {
    countries[0]: "Kyiv",
    countries[1]: "Madrid",
    countries[2]: "Rome", }

for country, capital in countries_capitals.items():
    print(f"{country}: {capital}")
