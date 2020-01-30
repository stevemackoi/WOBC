#arg1 = sys.argv[1]

def check_letter_frequency(x):
    with open(x) as f:
        openFile = (f.read())
        upper = openFile.upper()
    letter_frequency_dict = dict()
    for word in upper:
        for letter in word:
            if letter in letter_frequency_dict:
                letter_frequency_dict[letter] += 1
            else:
                letter_frequency_dict[letter] = 1

    sorted_letter_frequency = [(key, letter_frequency_dict[key]) for key in sorted(letter_frequency_dict, key=letter_frequency_dict.get, reverse=True)]
    for key, value in sorted_letter_frequency:
        print('{} is the most common letter. It occurs {} times.'.format(key, value))

check_letter_frequency('large.txt')