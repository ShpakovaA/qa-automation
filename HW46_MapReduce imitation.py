import random
import os
import string
from threading import Thread
import time


def file_generator(directory, number_of_files, size):

    file_size = int(random.uniform(size / 2, size))
    os.makedirs(os.path.basename(directory), exist_ok=True)

    for n in range(number_of_files):

        file_name = "test" + str(n) + ".txt"
        file_path = os.path.join(directory, file_name)
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


def count_in_files(directory, files, letter_to_find, result=None):
    if result is None:
        result = []
    count = 0
    for file in files:
        path = os.path.join(directory, file)
        with open(path, "r") as f:
            text = f.read()
            count += text.count(letter_to_find)
    result.append(count)
    return count


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    directory_files = os.listdir(directory)
    files_in_directory = len(directory_files)
    files_per_thread = max(1, round(files_in_directory / number_of_threads))
    files_for_threads = []

    for i in range(0, files_in_directory, files_per_thread):
        files = directory_files[i:i + files_per_thread]
        files_qty = len(files)

        if len(files_for_threads) == number_of_threads:

            for n in range(files_qty):
                dif = files_in_directory-i
                dif -= n
                files_for_threads[dif].append(files[n])
        else:
            files_for_threads.append(files)

    result = []
    threads = []

    for files in files_for_threads:
        thread = Thread(target=count_in_files, args=(directory, files, letter_to_find, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(result)


file_generator("new_dir", 50, 500)

start_time = time.time()
print(letter_counter_in_one_thread_2("new_dir", "B"))
end_time = time.time()
print(end_time-start_time)

print()

start_time = time.time()
print(letter_counter_in_n_threads("new_dir", "B", 22))
end_time = time.time()
print(end_time-start_time)

