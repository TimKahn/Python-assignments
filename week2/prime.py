n = int(raw_input('Enter a positive integer to test primality:'))

prime = 'prime.'

if n <= 3: pass
elif n%2 == 0: prime = 'not prime.'
else:
    sqrt_n = int(n**(.5)) #largest possible factor
    for number in range(3, sqrt_n, 2):
        if n%number == 0: prime = 'not prime.'

print 'The number entered is ' + prime
