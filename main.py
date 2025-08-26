from stats import number_of_words
from stats import number_of_characters
from stats import sorting
import sys


def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        file_contents = f.read()
        return file_contents


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    entire_book = get_book_text(sys.argv[1])
    num_words = number_of_words(entire_book)
    num_characters = number_of_characters(entire_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    sorted_characters = sorting(num_characters)
    for sorted_character in sorted_characters:
        print(f"{sorted_character["char"]}: {sorted_character["num"]}")
    print("============= END ===============")


main()