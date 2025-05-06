from stats import get_word_count, get_char_count, char_sorter
import sys

# Functions

## get book text from file ##

def get_book_text(file_path):
    ## get file
    with open(file_path) as f:
        book_text = f.read() ## converts to text
    return book_text         ## returns the text



## main ##
def main(): ## main function
    #
    book_text = get_book_text("books/frankenstein.txt") 
    word_count = get_word_count(book_text) # gets word count
    char_count = get_char_count(book_text) # gets char count
    sorted_char_count = char_sorter(char_count) # sorts chars by count
    ## print results
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    
    for item in sorted_char_count:
        print(f"{item['char']}: {item['count']}") # prints sorted char count

    print("============= END ===============")
    return book_text

    

    

if __name__ == "__main__":
    main()    