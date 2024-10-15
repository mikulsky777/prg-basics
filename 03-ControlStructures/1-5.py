total_tasks = 20
tasks_ok = int(input('Enter how many taksk have you completed: '))
test_passed = False

if (tasks_ok / total_tasks)*100 >=50 :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')