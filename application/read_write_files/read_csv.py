import csv


def read_csv(file):
    with open(file, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    return contacts_list

