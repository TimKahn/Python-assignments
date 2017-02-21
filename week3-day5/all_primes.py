def primes(input):
    prime_list = range(1, input + 1)
    for n in range(4, input + 1, 2): #remove evens except 2
        prime_list.remove(n)
    for item in prime_list[2:]: #remove multiples of remaining items starting with their squares
        for m in range(item, (input + 1)//item, 2):
            if item*m in prime_list: prime_list.remove(item*m)
    return prime_list
