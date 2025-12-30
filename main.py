from stats import word_count, char_count, sort_dict, build_report
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#file_path = "books/frankenstein.txt"
file_path = sys.argv[1]
count = word_count(file_path)
characters = char_count(file_path)
sorted_characters = sort_dict(file_path)


print(
f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------"""
)
for item in sorted_characters:
    if item["char"].isalpha():
        print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")
#print(f"Found {count} total words")


