# Email address validator

email = "aaa@bbb.ccc"
#email = "@aaabbb.ccc"
#email = "aaa@bbbccc."
#email = "aaa@bbbccc"
#email = "aaabbb.ccc"
#email = "@aaabbbccc."
#email = "aa@bbb.c>c"
#email = "a@a@bbb.ccc"
#email = "aa@bbb.cc.c"
#email = "aa.bbb@ccc"
#email = "aa.a@bbb.ccc"
#email = "@aaa.bb$b@cc.l@^c."

result = True
starts_ends_with_symbol = email.startswith("@") or email.endswith(".")
symbol_used_once = email.count("@") == 1 and email.count(".") == 1
at_before_dot = email.find("@") < email.find(".")

if not starts_ends_with_symbol and symbol_used_once and at_before_dot:
    for symbol in email:
        if not symbol.isalpha() and not symbol.isdigit() and symbol != "@" and symbol != ".":
            result = False
else:
    result = False
print(result)
