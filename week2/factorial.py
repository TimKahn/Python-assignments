n = int(raw_input('Enter a nonnegative integer to compute factorial:'))

factorial = 1
for num in range(1, n+1):
    factorial = factorial*num

print factorial
