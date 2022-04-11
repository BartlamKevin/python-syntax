def print_upper_words(words):
    """Prints each word uppercased
        print_upper_words(["here","are","some","words"])
        HERE
        ARE
        SOME
        WORDS    
    """
    for word in words:
        print(word.upper())

def print_e_words(words):
    """Prints each word that starts with e/e uppercased
        print_upper_words(["edge","Edward","Rydia","cid"])
        EDGE
        EDWARD    
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_these_letter_words(words,must_start_with):
    """Prints each word that starts with specified letter uppercased
        print_upper_words(["Alphinaud","Fordola","Thancred","Alisae","Y'shtola","Hilda"],
        ...    must_start_with=["F", "H"])
        FORDOLA
        HILDA   
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                