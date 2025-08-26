from stats import num_words, character_num_times


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



def main():
    book_text= get_book_text("books/frankenstein.txt")
    print(get_book_text("books/frankenstein.txt"))
    words= num_words(book_text)
    count= character_num_times(book_text)
    print(f"\n {words} words found in the document \n")
    print(count)


main()



	
