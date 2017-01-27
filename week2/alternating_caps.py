import string

your_string = str(raw_input('Enter a string to see it in alternating caps:'))
new_string = ''
letter_count = 0

for n in range(0, len(your_string)):
    if your_string[n] in string.ascii_letters:
        if letter_count%2 == 0:
            new_string += your_string[n].upper()
        else:
            new_string += your_string[n].lower()
        letter_count += 1
    else:
        new_string += your_string[n]

print new_string
