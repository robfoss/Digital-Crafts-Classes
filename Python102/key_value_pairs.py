#Dictionaires in Python

movie = {
    'name': 'Star Wars',
    'episode': 4,
    'year': '1977',
    'villians': ['Vader', 'Tarkin'],
    'heros': ['Luke', 'Leia', 'Han']
}

print(movie)
print(movie['year'])
bad_guys = movie['villians']

movie['ships'] = ['Falcon', 'Death Star']

for key in movie:
    print(key, movie[key])