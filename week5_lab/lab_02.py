# Find the Frequency of Each Word

file_path = "week5_lab_data/input1.txt"
def word_frequencies(file_path : str) -> dict[str, int]:
    from collections import Counter
    result = dict()
    with open(file_path) as f_read:
        for line in f_read:
            for w in line.lower().split():
                result[w] = result.get(w, 0) + 1
    return result

print(word_frequencies(file_path))