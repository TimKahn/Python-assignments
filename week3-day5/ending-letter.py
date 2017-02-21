def end(word_list, letter):
    answers = [word for word in word_list if word[-1] == letter]
    return answers
