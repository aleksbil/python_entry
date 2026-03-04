import random
names = [
    'Balerion',
    'Eldarion',
    'Smaug', 
    'Artemis',
    'Draco',
    'Fenrir',
    'Azrael',
    'Morwen',
    'Ragnar',
    'Saphira'
]

res = random.choice(names)
name = input('What is your name?: ')
if name == 'Geralt':
    print(f'{name}, meet your horse, Płotka')
else: print(f'{name}, meet your horse, {res}' )