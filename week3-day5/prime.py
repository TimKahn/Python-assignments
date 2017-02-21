def chk_prime(n=0):
    is_prime = ''

    if n > 3 and n % 2 == 0: is_prime = ' not'
    else:
        for num in range(3, int(n**(0.5)), 2):
            if n % num == 0:
                is_prime = ' not'
                break
    return 'The number you inputted is'+is_prime+' prime.'
