# Email address validator using regular expressions
import re

email = "aaa@bbb.ccc"
# email = "aa_a@bbb.ccc"
# email = "@aaab bb.ccc"
# email = "a_aa@bbbccc."
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
    if re.fullmatch(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', email):
        return True
    else:
        return False


print(email_validator_1(email))
