def avg_speed(distance,hours,minutes):
    hours = hours + minutes / 60
    speed = distance / hours
    return speed

n1 = int(input("Enter distance in km: "))
n2 = int(input("Enter number of travel hours: "))
n3 = int(input("Enter number of travel minutes: "))
result = round(avg_speed(n1,n2,n3), 1)
print(f'Average speed: {result} km/h')