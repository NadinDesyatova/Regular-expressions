from application.list_conversion import list_conversion
from application.read_write_files.read_csv import read_csv
from application.read_write_files.write_csv import write_csv




if __name__ == '__main__':
    contacts_list = read_csv("phonebook_raw.csv")

    new_contacs_list = list_conversion(contacts_list)

    write_csv("phonebook.csv", new_contacs_list)
