n1 = int(input("Enter distance in km: "))
n2 = int(input("Enter number of travel hours: "))
n3 = int(input("Enter number of travel minutes: "))

avg_speed = lambda distance, hours, minutes: distance / (hours + minutes/60)

result = round(avg_speed(n1,n2,n3), 1)
print(f'Average speed: {result} km/h')