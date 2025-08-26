from stats import num_words, character_num_times, sorted_list
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



def main():
    #book_text= get_book_text("books/frankenstein.txt")
    if len(sys.argv) == 1:
        print("\n Usage: python3 main.py <path_to_book>\n")
        sys.exit(1)
    else:
        book_text= get_book_text(sys.argv[1])
        #print(get_book_text("books/frankenstein.txt"))
        print("\n ============ BOOKBOT ============ \n Analyzing book found at books/frankenstein.txt...")
        words= num_words(book_text)
        count= character_num_times(book_text)
        sorted_count= sorted_list(count)
        print(f"\n----------- Word Count ---------- \n Found {words} total words \n--------- Character Count -------\n")
        for item in sorted_count:
            if not item['char'].isalpha():
                continue
            print(f'{item["char"]}: {item['num']}')
        print(sys.argv)


main()



	
