def pts_to_grade(points):
    grade = ['Fail','Satisfactory','Good','Excellent']
    if points >= 18:
        grade = grade[3]
    elif points >= 14:
        grade = grade[2]
    elif points >= 10:
        grade = grade[1]
    elif points < 10:
        grade = grade[0]
    return grade

test_result = 18
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')