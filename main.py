from stats import count_words, count_letters, sort_letters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count_words(sys.argv[1])
    count_letters(sys.argv[1])
    sorted_letters = sort_letters(sys.argv[1])
    for i in sorted_letters:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()