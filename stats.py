def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
        return(file_content)

def main(filepath):
    content = get_book_text(filepath)
    return content

def word_count(filepath):
    book = main(filepath)
    book_length = len(book.split())
    return book_length

def char_count(filepath):
    book = main(filepath)
    characters = {}
    for char in book:
        item = char.lower()
        characters[item] = characters.get(item, 0) + 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dict(filepath):
    original = char_count(filepath)
    sorted_dict = []
    for key, value in original.items():
        new_entry = {"char" : key, "num" : value}
        sorted_dict.append(new_entry)
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def build_report(filepath):
    count = word_count(filepath)
