def get_num_words(book):
    word_len = book.split()

    return len(word_len)

def get_num_chars(book):
    chars = {}
    for word in book.split():
        for char in word.lower():
            chars[char] = chars.get(char, 0) + 1

    return chars


