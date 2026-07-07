def word_count(book_text):
    words = book_text.split()
    number_of_words = len(words)
    return number_of_words

def character_count(book_text):
    lowercased_chars = book_text.lower()
    char_counter = {}
    for char in lowercased_chars:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter

def sort_on(tuple):
    return tuple[1]

def chars_dict_to_sorted_list(char_dict):
    new_list = []
    for char in char_dict:
         first_part = char
         second_part = char_dict[char]
         tuple_to_add = (first_part, second_part)
         new_list.append(tuple_to_add)
    sorted_list = sorted(new_list, reverse=True, key=sort_on)
    return sorted_list
