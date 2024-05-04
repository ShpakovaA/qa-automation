# Combining files
import os

directory_name = "source_directory"
matched_files = {}

for root, dir, files in os.walk(directory_name):
    for file in files:

        file_size = os.path.getsize(os.path.join(root, file))

        if os.path.basename(file).endswith(".txt") and file_size <= 120:
            matched_files[file] = root

with open("combined_file.txt", "w") as f:

    for file in matched_files:
        path = os.path.join(matched_files[file], file)

        with open(path, "r") as input:
            f.write(file)
            f.write("\n")
            f.write(input.read())
            f.write("\n")

