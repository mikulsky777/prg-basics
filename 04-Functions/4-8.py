def time_strings(hours, minutes, time_format):
    if time_format == "'24":
        if hours < 10 and minutes < 10:
            print(f'0{hours}:0{minutes}')
        elif hours < 10 and minutes > 10:
            print(f'0{hours}:{minutes}')
        elif hours > 10 and minutes < 10:
            print(f'{hours}:0{minutes}')
        elif hours > 10 and minutes > 10:
            print(f'{hours}:{minutes}')

    elif time_format == "'12":
        if hours < 12:
            if minutes < 10:
                print(f'{hours}:0{minutes}am')
            elif minutes >= 10:
                print(f'{hours}:{minutes}am')
        elif hours > 12:
            if minutes < 10:
                print(f'{hours-12}:0{minutes}pm')
            elif minutes >= 10:
                print(f'{hours-12}:{minutes}pm')
        elif hours == 0:
            if minutes < 10:
                print(f'0{hours}:0{minutes}am')
            elif minutes >= 10:
                print(f'0{hours}:{minutes}am')
        elif hours == 12:
            if minutes < 10:
                print(f'{hours}:0{minutes}pm')
            elif minutes >= 10:
                print(f'{hours}:{minutes}pm')

time_strings(0,10,"'12")