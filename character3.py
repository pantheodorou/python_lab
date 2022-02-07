from collections import Counter


def filter_ascii_codes(ascii_code_list: list) -> list:
    """
    Φιλτράρει μια λίστα με ascii codes και αφήνει μόνο το κενό και γράμματα
    κεφαλαία και μικρά
    """
    SPACE = 32
    capitals = list(range(65, 91))
    small = list(range(97, 123))
    valid = [SPACE] + capitals + small
    filtered = []
    for elm in ascii_code_list:
        if elm in valid:
            filtered.append(elm)
    return filtered


def ascii_codes2char(ascii_codes: list) -> str:
    """
    Μετατρέπει μια λίστα με ascii codes σε δεκαδική μορφή σε κείμενο
    """
    return ''.join([chr(i) for i in ascii_codes])


def remove_pairs_of_length(words: list, len2remove=20) -> list:
    """
    Σε μια λίστα με λέξεις βρίσκει τα ζευγάρια των λέξεων που το μέγεθός τους
    αθροιζόμενο είναι len2remove και τις αφαιρεί.
    """
    for_delete = []
    for i, wleni in enumerate(words[:-1]):
        for j, wlenj in enumerate(words[i+1:]):
            if len(wleni) + len(wlenj) == len2remove:
                if i not in for_delete and (i+j+1) not in for_delete:
                    print(wleni, wlenj)
                    for_delete.append(i)
                    for_delete.append(i+j+1)
    return [words[i] for i in range(len(words)) if i not in for_delete]


def ascii_edit(filename: str):
    char_ascii = ''
    with open(filename, encoding='utf8') as fil:
        char_ascii = fil.read()
    ascii_codes = [ord(i) for i in char_ascii]
    filtered_list = filter_ascii_codes(ascii_codes)
    filtered_text = ascii_codes2char(filtered_list)
    word_list = filtered_text.split()
    filtered_without_pairs_list = remove_pairs_of_length(word_list, 20)
    print(' '.join(filtered_without_pairs_list))
    final_word_sizes = [len(i) for i in filtered_without_pairs_list]
    # print('final:', final_word_sizes)
    fdic = dict(Counter(final_word_sizes))
    for size in sorted(fdic):
        print(f"Λέξεις με {size} γράμματα : {fdic[size]}")


if __name__ == '__main__':
    ascii_edit('sample_ascii.txt')
    # print(remove_pairs(['ta', 'abcdefghqwwe', 'from', 'qqqqaaaa']))
