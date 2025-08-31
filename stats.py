def get_book_words(book_contents):
    num_words = 0
    for word in book_contents.split():
        num_words += 1
    return num_words

def counting_characters(book_contents):
    characters = {}
    for c in book_contents:
        char = c.lower() 
        characters[char] = characters.get(char, 0) + 1
    return characters

def sort_on(item):
    return item["num"]

def sorted_characters(characters):
    sorted_char = []
    for ch, count in  characters.items():
        if ch.isalpha() == True:
            sorted_char.append({"char": ch, "num": count})
            sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char
    

