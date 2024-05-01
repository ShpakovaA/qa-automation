# Search words by condition
string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

#Option1
result = ""

for word in string.split():
    print(word)

    if "oo" in word.lower():
        result += word.title() + " "

print(result)


#Option2
result = []

for word in string.split():
    print(word)

    if "oo" in word.lower():
        result.append(word.title())

print(" ".join(result))
