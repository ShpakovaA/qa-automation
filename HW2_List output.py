# List output

pets_names = ["Nike", "Lota", "Vincent"]

for i, name in enumerate(pets_names):
    if i == len(pets_names)-1:
        print(name)
    else:
        print(name, end=", ")

