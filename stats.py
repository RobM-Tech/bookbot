

## data analysis ##

def get_word_count(book_text): ## get book_text from main()
    #
    words = book_text.split()    ## split text
    word_count = len(words) ## count words
    return word_count       ## returns word count

def get_char_count(book_text): ## gets total count of characters
    #
    char_dic = {}
    
    for l in book_text.lower():
        if l not in char_dic:
            char_dic[l] = 1
        else:
            char_dic[l] += 1
    return char_dic
            
