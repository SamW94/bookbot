def book_to_string(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    character_count = {}
 
    for char in lowered_text:
        character_count[char] = character_count.get(char, 0) + 1

    return character_count

def print_character_count_report(character_count_dictionary):
    def sort_on(dict):
        return dict["count"]
    
    list_of_character_counts = []
    for character in character_count_dictionary:
        list_of_character_counts.append({"character": character, "count": character_count_dictionary[character]})
        
    list_of_character_counts.sort(reverse=True, key=sort_on)
    
    for dictionary in list_of_character_counts:
        if (dictionary['character']).isalpha():
            print(f"The '{dictionary['character']}' character was found {dictionary['count']} times")

def main():
    try: 
        whole_book_string = book_to_string("books/frankenstein.txt")
        word_count = count_words(whole_book_string)
        character_count_dictionary = count_characters(whole_book_string)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print_character_count_report(character_count_dictionary)
        print("--- End report ---")
    except FileNotFoundError as error:
        print(f"{error}\nIs your file name entered correctly?")

if __name__ == '__main__':
    main()
