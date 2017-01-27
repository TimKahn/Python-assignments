your_string = str(raw_input('Enter any string:'))
letter = str(raw_input('Now enter a letter to count its occurrences:'))

count = 0
for char in your_string:
    if char == letter: count += 1

print 'The letter ' + letter + ' occurs ' + str(count) + ' times.'
