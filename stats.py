def get_num_words(book):
    word_len = book.split()

    return len(word_len)

def get_num_chars(book):
    chars = {}
    for word in book.split():
        for char in word.lower():
            chars[char] = chars.get(char, 0) + 1

    return chars

def sort_on(items):
    return items["num"]

def get_sorted_chars(chars_dict):
    sorted_dict = []
    for k, v in chars_dict.items():
        sorted_dict.append({"char": k, "num":v})

    sorted_dict.sort(reverse=True, key=sort_on)

    return sorted_dict


