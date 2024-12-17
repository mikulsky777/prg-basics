number = int(input("enter speed(m/s): "))
ms_to_kmh = lambda ms: ms * 3.6
result = ms_to_kmh(number)
print(f'{number} m/s = {result} km/h')