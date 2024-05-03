# Sum and product of list elements by condition

lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
#lst = [1, 1, 1, 1, 1, 1, 9, 1, 1]
MIN = 3
MAX = 6
elements_sum = 0
product = 1
isFound = False

for element in lst:
    if element >= MIN and element <= MAX:
        elements_sum += element
        product *= element
        isFound = True

if not isFound:
    elements_sum = None
    product = None

print(elements_sum, product) #sum_ = 20, product = 576