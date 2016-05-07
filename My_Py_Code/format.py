print()
print('Hello, {::^30}' .format('World'))
print()
print('{0}, {1}, {2}' .format('first', 'second', 'third'))
print()
print("Coordinates: {latitude}, {longitude}" .format(latitude='37.24N', longitude='-115.81W'))
print()
string = ('Two beers')

if string:
    print('The string is {}'.format(string))
else:
    print('Число равно нулю')
print()
coord = (3, 5)
print('X: {0[0]}; Y: {0[1]}'.format(coord))

print()
points = 19.5
total = 32
print('Correct answers: {:.2%}'.format(points/total))
print()