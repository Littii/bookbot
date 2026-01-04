def get_book_text(path):
    with open(path) as text:
        book = text.read()
        return book

def count_words(path):
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    book_content = get_book_text(path)
    book_list = book_content.split()
    num_words = len(book_list)
    print(f"Found {num_words} total words")

def count_letters(path):
    book_content = get_book_text(path).lower()
    letter_count_dict = {}
    for let in range(0,len(book_content)):
        if book_content[let] in letter_count_dict:
            letter_count_dict[book_content[let]]+=1
        else:
            letter_count_dict[book_content[let]]=1
    return letter_count_dict

def sort_on(letter_split_list):
    return letter_split_list["num"]

def sort_letters(path):
    print("--------- Character Count -------")
    letter_split_list = []
    one_letter_dict = {}
    letter_count_dict = count_letters(path)
    for letter in letter_count_dict:
        if letter.isalpha():
            one_letter_dict = {"char": letter, "num": letter_count_dict[letter]} 
            letter_split_list.append(one_letter_dict)
    letter_split_list.sort(key=sort_on, reverse=True)
    return letter_split_list