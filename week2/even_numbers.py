n = int(raw_input('I want to see all even numbers between zero and:'))

evens = []
for num in range(0,n+1,2):
    evens.append(num)

print evens
