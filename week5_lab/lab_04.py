# Replace Specific Words

from typing import List, Dict, Any

dict_words = {
    "intelligence": "Intel",
    "computer": "Computer",
    "artificial": "Artificial",
    "human": "Human",
    "problem": "Issue",
    "learning": "Studying"
}

file_path = "week5_lab_data/input5.txt"

def replace_words(file_path: str, replacements: Dict[str, str]) -> None:
    with open(file_path, 'r') as file:
        content = file.read()

    for old_word, new_word in replacements.items():
        content = content.replace(old_word, new_word)

    return content



# def replace_specific_words(file_path):
#     import re
#     with open(file_path) as f_read:
#         for line in f_read:
#             for word in dict_words:
#                 re.sub(r'[word]', dict_words[word], line)


# replace_specific_words(file_path)
result1 = replace_words(file_path, dict_words)
print(result1)