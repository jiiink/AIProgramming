#Count Unique Words

file_path = "week5_lab_data/input1.txt"
def count_unique_words(file_path : str) -> int:
    import re
    result = dict()
    with open(file_path) as f_read:
        for line in f_read:
            for w in line.lower().split():
                w = re.sub(r'[^\w\s]', '', w)
                result[w] = result.get(w, 0) + 1
        return len(result)

def count_unique_words2(file_path: str) -> int:
    from itertools import chain
    import re

    with open(file_path) as f_read:
        return len(set(chain(*[re.sub(r'[^\w\s]', '', line).lower().split() for line in f_read.readlines()])))





print(count_unique_words(file_path))

print(count_unique_words2(file_path))