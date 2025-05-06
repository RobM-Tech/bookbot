

# Functions

## get book text from file ##

def get_book_text(file_path):
    # Read the book text from the file
    with open(file_path) as f:
        book_text = f.read()
    return book_text

## data analysis ##

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

## main ##
def main():
    #
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document.")
    return text

if __name__ == "__main__":
    main()    