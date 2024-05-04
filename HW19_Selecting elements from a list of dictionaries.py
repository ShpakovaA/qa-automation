# Selecting elements from a list of dictionaries

users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19}
]

# Result: ['Olaf Andvarafors', 'Brun Du Barnstokr']

result = [user["name"] for user in users if user["age"] >= 18]
print(result)
