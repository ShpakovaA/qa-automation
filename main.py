def check_email(email):
    if '@' in email:
        return True
    else:
        return False


test_data = [
    ("aaa123@bbb.ccc", True),
    ("aaabbb.ccc", False),
    ("aaa@bbbccc", False),
    ("a@aa@bbb.ccc", False),
    ("aaa@bbb.cc.c", False),
]

for email, expected_result in test_data:

        observed_result = check_email(email)
        assert observed_result is expected_result, f"Expected to get {expected_result} but got {observed_result} for {email}"
