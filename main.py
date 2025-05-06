from stats import get_word_count, get_char_count


# Functions

## get book text from file ##

def get_book_text(file_path):## Read the book text from the file
    #
    with open(file_path) as f:
        book_text = f.read() ## converts file to text
    return book_text         ## returns the text



## main ##
def main(): ## main function
    #
    book_text = get_book_text("books/frankenstein.txt") 
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    print(f"{word_count} words found in the document.")
    print(f"{char_count}")
    return book_text

if __name__ == "__main__":
    main()    