your_string = str(raw_input('Enter a string to see it disemvoweled:'))

vowels = ['a','e','i','o','u']
new_string = ''

for char in your_string:
    if char in vowels: continue
    new_string += char

print new_string
