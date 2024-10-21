total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if extra_rinse == 'y':
    extra_rinse = True
    total_washing_time += 15
elif extra_rinse == 'n':
    extra_rinse = False

if extra_spin == 'y':
    extra_spin = True
    total_washing_time += 9
elif extra_spin == 'n':
    extra_spin = False


if program == 'j':
    washing_product = 'jacket'
    total_washing_time += 40
elif program == 'u':
    washing_product = 'underwear'
    total_washing_time += 70
elif program == 's':
    washing_product = 'shoes'
    total_washing_time += 20


print(f'washing_product = {washing_product}')
print(f'rinse = {extra_rinse}')
print(f'spin = {extra_spin}')
print(f'Total washing time: {total_washing_time}')