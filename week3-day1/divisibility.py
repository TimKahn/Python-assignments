def divisible(number_list, divisor):
    answers = ['yes' if num%divisor == 0 else 'no' for num in number_list]
    return answers
