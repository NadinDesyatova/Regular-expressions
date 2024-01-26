import csv


def write_csv(file, list):
    with open(file, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list)
