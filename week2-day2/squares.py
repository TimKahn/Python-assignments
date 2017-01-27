user_input = str(raw_input('Enter some numbers separated by dashes: '))
input_list = user_input.split('-')

squares = {}
for elem in input_list:
    squares[int(elem)] = (int(elem))**2

print squares
