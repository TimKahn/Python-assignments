factor = int(raw_input('Enter a number to see its multiples: '))
end_with = int(raw_input('Print only multiples between (not including) zero and: '))

multiples = []
for num in range(factor, end_with, factor):
    multiples.append(num)

print multiples
