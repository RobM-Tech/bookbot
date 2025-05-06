

# Functions

## get book text from file ##

def get_book_text(file_path):
    # Read the book text from the file
    with open(file_path) as f:
        book_text = f.read()
    return book_text

## main ##
def main():
    #
    text = get_book_text("books/frankenstein.txt")
    print(text)
    return text

if __name__ == "__main__":
    main()
    