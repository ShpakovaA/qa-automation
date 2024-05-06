# Selecting items from several lists

test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

test_design_writers_set = set(test_design_writers)
test_scripters_set = set(test_scripters)
reviewers_set = set(reviewers)
out_of_office_today_set = set(out_of_office_today)

# all testers in the team
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
all_testers_set = {*test_design_writers, *test_scripters, *reviewers}
all_testers_list = sorted(all_testers_set)
print(all_testers_list)

# testers who can only write scripts
# [4, 6, 7, 8]
only_test_scripters_set = test_scripters_set - test_design_writers_set-reviewers_set
only_test_scripters_list = sorted(only_test_scripters_set)
print(only_test_scripters_list)

# testers who are at work today
# [3, 4, 7, 8, 9, 10]
at_work_today_set = all_testers_set - out_of_office_today_set
at_work_today_list = sorted(at_work_today_set)
print(at_work_today_list)

# testers who could write and review scripts, and are at work today
# [3]
sript_writers_reviewers_at_work_set = at_work_today_set & test_design_writers_set & reviewers_set
sript_writers_reviewers_at_work_list = sorted(sript_writers_reviewers_at_work_set)
print(sript_writers_reviewers_at_work_list)