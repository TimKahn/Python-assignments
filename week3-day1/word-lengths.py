def lengths(input = 'Any string', delimiter = ' '):
    words = input.split(delimiter)
    word_lengths = [len(item) for item in words]
    return word_lengths
