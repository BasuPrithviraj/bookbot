#global_alpha_numeric = {}

def num_words(text):
    words= text.split()
    return len(words)


def character_num_times(text):
    lower_text= text.lower()
    alpha_numeric = {} 
    for letter in lower_text:

        if letter in alpha_numeric:
            alpha_numeric[letter] = alpha_numeric[letter] + 1
        else:
            #num_letters = lower_text[letter]
            alpha_numeric[letter] = 1
    #print(alpha_numeric)

    #global_alpha_numeric= alpha_numeric

    return alpha_numeric



def sort_on(items):
    return items["num"]


def sorted_list(unsorted_character):
    alpha_numeric_list = [{"char": char, "num": num} for char, num in unsorted_character.items()]
    alpha_numeric_list.sort(reverse=True, key=sort_on)
    return alpha_numeric_list

    
    #return item["num"]

