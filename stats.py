

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

    return alpha_numeric
