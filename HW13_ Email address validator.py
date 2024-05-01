# Email address validator

#email = "aaa@bbb.ccc"
#email = "@aaabbbccc."
email = "!aa@bbb.c>c"
#email = "a@a@bbb.ccc"
#email = "aa.a@bbb.ccc"
#email = "@aaa.bb$b@cc.l@^c."
result = False

if not email.startswith("@"):
    if not email.endswith("."):
        if len(email.split("@")) == 2 and len(email.split(".")) == 2:
            if email.find("@") < email.find("."):
                for symbol in email:
                    if not symbol.isalpha():
                        if not symbol.isdigit():
                            if symbol == "@" or symbol == ".":
                                result = True
                            else:
                                result = False
print(result)


