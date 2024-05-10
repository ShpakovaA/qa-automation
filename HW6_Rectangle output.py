height = int(input("Enter height of rectangular: "))
width = int(input("Enter width of rectangular: "))
symbol = input("Enter symbol to build rectangular with: ")
h = 0
w = 0
my_str = ""

while h < height:
    while w < width:
        my_str += symbol
        w += 1
    print(my_str)
    h += 1
