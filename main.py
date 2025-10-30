from stats import get_num_words, get_num_chars, get_sorted_chars
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        num_words = get_num_words(book)
        print(f" Found {num_words} total words")
        chars = get_num_chars(book)
        sorted_chars = get_sorted_chars(chars)
        for item in sorted_chars:
            if item["char"].isalpha(): print("{}: {}".format(item["char"], item["num"]))

main()
