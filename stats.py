def number_of_words(entire_book):
    words = []
    words = entire_book.split()
    word_count = len(words)
    return word_count


def number_of_characters(entire_book):
    lower_case_content = entire_book.lower()
    characters = {}
    for character in lower_case_content:
        characters[character] = characters.get(character, 0) +1
    return characters


def sort_on(items):
    return items["num"]

def sorting(characters):
    final_list = []
    for char, num in characters.items():
        if char.isalpha():
            char_info = {}
            char_info["char"] = char
            char_info["num"] = num
            final_list.append(char_info)
    final_list.sort(reverse=True, key=sort_on)
    return final_list