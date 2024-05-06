# Combining files
import os

directory_name = "source_directory"
matched_files_list = []

for root, dir, files in os.walk(directory_name):
    for file in files:

        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)

        if os.path.basename(file).endswith(".txt") and file_size <= 120:
            matched_files_list.append(file_path)

with open("combined_file.txt", "w") as f:

    for file in matched_files_list:
        with open(file, "r") as input:
            f.write(os.path.basename(file))
            f.write("\n")
            f.write(input.read())
            f.write("\n")

