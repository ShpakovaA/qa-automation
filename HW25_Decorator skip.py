def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not condition:
                return func(*args, **kwargs)
            if reason != '':
                print(reason)

        return wrapper

    return decorator

@skip_if(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5


test_two_plus_two()  # 'Skipped because of JIRA-123 bug' is printed


@skip_if(condition=False, reason='Skipped because of JIRA-123 bug')
def test_two_minus_two():
    assert 2 - 2 == 5


test_two_minus_two()  # assertion error
