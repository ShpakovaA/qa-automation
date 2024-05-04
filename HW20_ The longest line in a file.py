#  The longest line in a file

longest_line = ""
file = "some_file.txt"

with open(file, "r") as f:
    data = f.read()

lines_lst = data.split('\n')

for line in lines_lst:
    if len(line) >= len(longest_line):
        longest_line = line

print(longest_line)
