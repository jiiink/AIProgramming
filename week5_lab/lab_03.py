# Read a CSV File into a List of Dictionaries

file_path = "week5_lab_data/input3.txt"


def read_csv3(file_path):
    from collections import defaultdict
    result = defaultdict(list)
    with open(file_path) as f_read:
        header = f_read.readline().rstrip().split(',')
        for line in f_read:
            cols = line.rstrip().split(',')
            for i in range(len(cols)):
                result[header[i]].append(cols[i])
    print(result)

def read_csv(file_path: str) -> list[dict[str, any]]:
    import csv
    from collections import defaultdict
    result = defaultdict(list)
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            for i, col in enumerate(row):
                result[header[i]].append(col)
    return dict(result)

# def read_csv2(file_path: str) -> list[dict[str, any]]:
#
#   import csv
#
#   with open(file_path) as csvfile:
#
#     reader = csv.reader(csvfile)
#
#     headers = next(reader)
#
#     data = zip(*reader)
#
#     return dict(zip(headers, data))





print(read_csv(file_path))
read_csv3(file_path)
# print(read_csv2(file_path))