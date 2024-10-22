def day_name(day_number):
    result = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if day_number == 1:
        result = result[0]
    elif day_number == 2:
        result = result[1]
    elif day_number == 3:
        result = result[2]
    elif day_number == 4:
        result = result[3]
    elif day_number == 5:
        result = result[4]
    elif day_number == 6:
        result = result[5]
    elif day_number == 7:
        result = result[6]
    return result

print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))