

## data analysis ##

def get_word_count(book_text):
    ## Counts the number of words in the provided text.
    words = book_text.split()    ## split text into words
    word_count = len(words)      ## get word count
    return word_count            ## return word count

def get_char_count(book_text):
    ## Counts the occurrences of each character in the provided text.
    char_dic = {} ## empty dictionary to store characters/counts
    
    ## loop through text, convert to lowercase , count ea char, add to dic
    for l in book_text.lower():
        if l not in char_dic:
            char_dic[l] = 1     ## if not in dic add and +1 count
        else:
            char_dic[l] += 1    ## +1 to characters count

    return char_dic ## return result to dictionary





def char_sorter(char_dic):
    #
    filter_dic = {k: v for k, v in char_dic.items() if k.isalpha()}

    char_list = [{"char": k, "count": v} for k, v in filter_dic.items()]
    
    def sort_on(char_dic):
        return char_dic["count"]
    
    char_list.sort(key=sort_on, reverse=True)
    
    return char_list



    
   