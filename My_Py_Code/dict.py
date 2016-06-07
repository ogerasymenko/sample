'''

Created on May 29, 2016.
Work with dictionaries.

'''

__author__ = 'sashko'


k = ['Audi', 'BMW', 'Ford']
v = ['A4', '320', 'Focus']
l = list(zip(k, v))
d = dict(zip(k, v))

print(l)
print(d)

keys = list(d.keys())
keys.sort()
for key in keys:
    print('{0} {1}'.format(key, d[key]))

my_dict = {'Audi': 'A4', 'BMW': '320', 'Ford': 'Focus', 'Jaguar': 'XE'}
print(my_dict)
