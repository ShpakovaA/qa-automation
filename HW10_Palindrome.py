# Palindrome
str = "    aBC cba " # True
#str = "a BCQcb a    " # True
#str = " ab bca"  # False
#str = "ab b a"  # False


# Way 1
formatted_str = str.strip().lower()
if formatted_str == formatted_str[::-1]:
    print(f"This string '{str}' is a palindrom")
else:
    print(f"This string '{str}' is not a palindrom")

# Way 2
formatted_str = str.strip().lower()
reversed_formatted_str = formatted_str[::-1]
if formatted_str.find(reversed_formatted_str) == 0:
    print(f"This string '{str}' is a palindrom")
else:
    print(f"This string '{str}' is not a palindrom")
