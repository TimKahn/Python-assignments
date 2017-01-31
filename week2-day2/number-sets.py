set1 = set(raw_input('Enter some numbers separated by commas: ').split(','))
set2 = set(raw_input('Now enter more numbers separated by commas to find numbers in common: ').split(','))
intersect = set1.intersection(set2)
print ', '.join(intersect)
