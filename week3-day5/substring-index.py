def substring_indices(string_list, substring):
    answers = [string_list.index(item) for item in string_list if substring in item]
    return answers
