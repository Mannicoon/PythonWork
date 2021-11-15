name = input('Sisesta nimi: ')

place = input('Sisesta elukoht: ')

age = input('Sisesta vanus: ')

print('-----------------------------------------')

if place == 'Saaremaa':
    print('Tere tulemast saarlane', name)

else:
    print('Tere tulemast,', name)

print('Teie elukoht on', place)

print('Teie vanus on', age)

print('-----------------------------------------')

x = int(age)

if x < 18:
    print('Te pole piisavalt vana et autoga sõita.')

if x == 18:
    print('Palju õnne! Te olete täiskasvanu.')

if x > 18:
    print('Te olete piisavalt vana, et autoga sõita.')

print('-----------------------------------------')

