import random
import os
import string
from threading import Thread


def file_generator(directory, number_of_files, size):
    for n in range(number_of_files):

        file_name = "test" + str(n) + ".txt"
        file_path = os.path.join(directory, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        file_size = int(random.uniform(size / 2, size))
        data = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=file_size))

        with open(file_path, "w") as file:
            file.write(data)


def letter_counter_in_one_thread_1(directory, letter_to_find):
    count = 0
    for root, dir, files in os.walk(directory):
        for file in files:

            file_path = os.path.join(root, file)

            with open(file_path, "r") as f:
                text = f.read()
                count += text.count(letter_to_find)
    return count


def letter_counter_in_one_thread_2(directory, letter_to_find):
    directory_files = os.listdir(directory)
    count = 0

    for file in directory_files:
        path = os.path.join(directory, file)

        with open(path, "r") as f:
            text = f.read()
            count += text.count(letter_to_find)

    return count



def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    pass
#
#
# def count_in_file(file, letter_to_find):
#     count = 0
#     with open(file, "r") as f:
#         text = f.read()
#         count += text.count(letter_to_find)
#     return count
#
#
#
#
# for number in range(7):
#     thread = Thread(target=count_in_file, args=("new_dir", "B"))
#     thread.start()

# print(count_in_file("new_dir/test4.txt", "B"))


threads_number = 7
directory_files = os.listdir("new_dir")
files_in_directory = len(directory_files)
n = 0
files_for_threads = []
while len(directory_files) % threads_number != 0:
    threads_number -= 1
files_in_threads = round(len(directory_files) / threads_number)

while n < len(directory_files):
    list = []
    for i in range(files_in_threads):
        list.append(directory_files[n])
        n += 1
    files_for_threads.append(list)


def count_in_files(directory, files, letter_to_find):
    count = 0
    for file in files:
        print(file)
        path = os.path.join(directory, file)
        with open(path, "r") as f:
            text = f.read()
            count += text.count(letter_to_find)

    return count


for number in range(len(files_for_threads)):
    thread = Thread(target=count_in_files, args=("new_dir", files_for_threads[number], "B"))
    thread.start()





# file_generator("new_dir", 5, 4)
# print(letter_counter_in_one_thread_1("new_dir", "B"))
# print(letter_counter_in_one_thread_2("new_dir", "B"))