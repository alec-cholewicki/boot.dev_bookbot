from stats import word_count, character_count, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath, encoding="utf-8-sig") as f:
        return f.read()

def print_report(filepath, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for tuple in sorted_chars:
        if tuple[0].isalpha():
            print(f"{tuple[0]}: {tuple[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Input the path to the book too! Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = word_count(book_contents)
    chars = character_count(book_contents)
    sorted_listed_chars = chars_dict_to_sorted_list(chars)
    print_report(book_path, num_words, sorted_listed_chars)

main()
