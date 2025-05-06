## data analysis ##

def get_word_count(book_text): ## get book_text from main()
    #
    words = book_text.split()    ## split text
    word_count = len(words) ## count words
    return word_count       ## returns word count