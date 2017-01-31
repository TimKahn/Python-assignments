import sys
user_input = ''
vocab = set([])

while True:
    user_input = str(raw_input("Enter a word to add to this script's vocabulary, v to view vocabulary, or q to quit: "))
    if user_input == 'q': sys.exit()
    elif user_input == 'v': print ' '.join(vocab)
    else: vocab.add(user_input)
