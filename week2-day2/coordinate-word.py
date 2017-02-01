import sys

user_input = []
dictionary = {}

while True:
    user_input = str(raw_input('Please enter a coordinate-word pair in the format: x,y,word: ')).split(',')
    if user_input == ['']: break
    new_key = tuple(user_input[0:2])
    new_value = user_input[2]
    dictionary[new_key] = new_value

query = ''

while True:
    query = str(raw_input('Please enter a coordinate to look up, or q to quit: '))
    if query == 'q': break
    coordinate = tuple(query.split(','))
    print dictionary.get(coordinate, 'Coordinate not found.')

sys.exit()
