# Email address validator

email = "aaa@bbb.ccc"
#email = "@aaabbbccc"
#email = "aaabbbccc."
#email = "@aaabbbccc."
#email = "!aa@bbb.c>c"
#email = "a@a@bbb.ccc"
#email = "aa.bbb@ccc"
#email = "aa.a@bbb.ccc"
#email = "@aaa.bb$b@cc.l@^c."

result = True
starts_ends_with_symbol = email.startswith("@") and email.endswith(".")
symbol_used_once = len(email.split("@")) == 2 and len(email.split(".")) == 2
at_before_dot = email.find("@") < email.find(".")

if not starts_ends_with_symbol and symbol_used_once and at_before_dot:
    for symbol in email:
        if not symbol.isalpha() and not symbol.isdigit() and symbol != "@" and symbol != ".":
            result = False
else:
    result = False
print(result)
