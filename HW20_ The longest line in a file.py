#  The longest line in a file

longest_line = ""
file = "some_file.txt"

with open(file, "r") as f:
    for line in f:

        if len(line) >= len(longest_line):
            longest_line = line

print(longest_line)
