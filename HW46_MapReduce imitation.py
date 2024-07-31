import random
import os
import string
from threading import Thread
import time


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

    # files_for_threads = []
    # for i in range(0, files_in_directory, files_per_thread):
    #     files_for_threads.append(directory_files[i:i+files_per_thread])
    files_for_threads = [directory_files[i:i+files_per_thread] for i in range(0, files_in_directory, files_per_thread)]

    result = []

    for i in range(len(files_for_threads)):
        thread = Thread(target=count_in_files, args=(directory, files_for_threads[i], letter_to_find, result))
        thread.start()
        thread.join()
    return sum(result)


def func_execution_time(func, *params):
    start_time = time.time()
    func(*params)
    end_time = time.time()
    return end_time - start_time


file_generator("new_dir", 50, 100)
print(letter_counter_in_one_thread_1("new_dir", "B"))
print(func_execution_time(letter_counter_in_one_thread_1, "new_dir", "B"))
print()
print(letter_counter_in_n_threads("new_dir", "B", 150))
print(func_execution_time(letter_counter_in_n_threads, "new_dir", "B", 150))
