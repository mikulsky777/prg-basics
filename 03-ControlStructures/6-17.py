time_24 = input("Enter time (24-hour format, hh:mm): ")

hours, minutes = time_24.split(':')

hours = int(hours)

if hours == 0:
    period = "am"
    hours_12 = 12  
elif hours == 12:
    period = "pm" 
elif hours > 12:
    period = "pm"
    hours_12 = hours - 12 
else:
    period = "am"
    hours_12 = hours  

print(f"Time in 12-hour format: {hours_12}:{minutes}{period}")