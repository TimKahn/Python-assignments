def letter_counter(filepath, letters_to_count):
    letter_dict = {}

    def build_dict():
        for char in letters_to_count.lower():
            letter_dict[char] = 0
        return letter_dict

    def read_file():
        

if __name__ == '__main__':
    letter_counter('test-file1.txt', 'aeiou')
