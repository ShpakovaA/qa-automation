# Email address validator using regular expressions
import re

email = "aaa@bbb.ccc"
# email = "@aaabbb.ccc"
# email = "aaa@bbbccc."
# email = "aaa@bbbccc"
# email = "aaabbb.ccc"
# email = "@aaabbbccc."
# email = "aa@bbb.c>c"
# email = "a@a@bbb.ccc"
# email = "aa@bbb.cc.c"
# email = "aa.bbb@ccc"
# email = "aa.a@bbb.ccc"
# email = "@aaa.bb$b@cc.l@^c."

def email_validator_1(email):
    if re.fullmatch(r'(\w+\@{1}\w+\.{1}\w+)', email):
        return True
    else:
        return False


print(email_validator_1(email))

def email_validator_2(email):
    if re.search(r'(^\w+\@{1}\w+\.{1}\w+$)', email):
        return True
    else:
        return False

print(email_validator_2(email))