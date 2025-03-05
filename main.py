from stats import get_word_count, get_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filepath>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    book_text = get_book_text(filepath)
    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f'Found {word_count} total words')
    print("----------- Character Count ----------")
    char_count = get_char_count(book_text)
    for item in char_count:
        print(f'{item}: {char_count[item]}')
main()