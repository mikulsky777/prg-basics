def ms_to_kmh(ms):
    kmh = ms * 3.6
    return kmh

number = int(input("enter speed(m/s): "))
result = ms_to_kmh(number)
print(f'{number} m/s = {result} km/h')