
#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '''\"Would you tell me, please, which way I ought to go from here?\"\n\"That depends a good deal on where you want to get to,\" said the Cat.\n\"I don't much care where ——\" said Alice.\n\"Then it doesn't matter which way you go,\" said the Cat.\n\"—— so long as I get somewhere,\" Alice added as an explanation.\n\"Oh, you're sure to do that,\" said the Cat, \"if you only walk long enough.\"'''
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
print("Task 02")
print("(:", alice_in_wonderland.find("("), ", ):", alice_in_wonderland.find(")"))
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("Task 03")
print(alice_in_wonderland)



"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
task04 = '''Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?'''

black_sea_area = 436402
azov_sea_area = 37800

print("Task 04")
print(task04)
print("Answer:\nThe total area of Black and Azov seas is Black Sea Area + Azov Sea Area:", black_sea_area+azov_sea_area, "sq.km")

# task 05
task05 ='''Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі'''
total_goods = 375291
storage1_and_storage2 = 250449
storage2_and_storage3 = 222950
storage_1 = total_goods - storage2_and_storage3
storage_3 = total_goods - storage1_and_storage2
storage_2 = total_goods - storage_3 - storage_1

print("Task 05")
print(task05)
print("Answer:\nStorage 1 has:",
      storage_1, "goods(total goods - goods in Storage 2 and Storage 3 together)\nStorage 3 has:",
      storage_3, "goods(total goods - goods in Storage 1 and Storage 2 together)\nStorage 2 has:",
      storage_2, "goods(total goods - goods in Storage 2 - goods in Storage 3)")

# task 06
task06 = '''Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.'''
monthly_payment = 1179
payment_period = 18
total_cost = monthly_payment * payment_period
print("Task 06")
print(task06)
print("Answer:\nTotal laptop cost is:", total_cost, "grn.(monthly payment * payment period)")

# task 07
task07 = '''Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9'''

answer_a = 8019 % 8
answer_b = 9907 % 9
answer_c = 2789 % 5
answer_d = 7248 % 6
answer_e = 7128 % 5
answer_f = 19224 % 9

print("Task 07")
print(task07)
print("Answer:\nThe reminder of a division for 8019 : 8 is", answer_a)
print("The reminder of a division for 9907 : 9 is", answer_b)
print("The reminder of a division for 2789 : 5 is", answer_c)
print("The reminder of a division for 7248 : 6 is", answer_d)
print("The reminder of a division for 7128 : 5 is", answer_e)
print("The reminder of a division for 19224 : 9", answer_f)


# task 08
task08 = '''Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн'''
big_pizza_price = 274
big_pizza_quantity = 4
big_pizza_total_price = big_pizza_price * big_pizza_quantity
medium_pizza_price = 218
medium_pizza_quantity = 2
medium_pizza_total_price = medium_pizza_quantity * medium_pizza_price
juice_price = 35
juice_quantity = 4
juice_total_price = 35
cake_price = 350
cake_quantity = 1
cake_total_price = cake_quantity * cake_price
water_price = 21
water_quantity = 3
water_total_price = water_price * water_quantity
total_price = water_total_price + juice_total_price + cake_total_price + big_pizza_total_price + medium_pizza_total_price
print("Task 8")
print(task08)
print("Answer:\nTotal amount of money needed:", total_price, "hrn (sum of each item quantity * it's price)")


# task 09
task09 = '''Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?'''

photos_quantity = 232
photos_per_page = 8
pages_needed = int(photos_quantity / photos_per_page)

print("Task 9")
print(task09)
print("Answer:\nThe amount of pages needed to place all photos is", pages_needed, "(total photos quantity / photos per page ")



# task 10
task10 = '''Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи повний бак?'''
distance = 1600
tank_capacity = 48
consumption = 9
gasoline_for_trip = distance * consumption / 100
gas_station_stops = int(gasoline_for_trip / tank_capacity)

print("Task 10")
print(task10)
print("Answers\n1)Total amount of gasoline needed for the trip is", gasoline_for_trip,
      "l. (total distance * consumption per 1 km) \n2)", gas_station_stops,
      "stops at gas station are required during the trip (total amount of gasoline required for trip / tanks capacity")