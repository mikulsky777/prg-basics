import math
height = input("Height of observation (in metres): ")
height = int(height)
distance = 3.57 * math.sqrt(height)
print("Your distance from the horizon is: ", distance, "kilometers")