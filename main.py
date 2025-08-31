import sys
from stats import get_book_words
from stats import counting_characters
from stats import sorted_characters
from stats import sort_on

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    num_words = get_book_words(book_contents)
    characters = counting_characters(book_contents)
    sorted_char = sorted_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        print(f"{item['char']}: {item['num']}")
   
   

def get_book_text(filepath):
    with open(filepath) as f:
        files_contents = f.read()
        return files_contents

main()

