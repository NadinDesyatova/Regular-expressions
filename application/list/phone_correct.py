import re


def phone_correct(contacts_list, index_phone_column):
    for i, item in enumerate(contacts_list):
        if i > 0:
            if item[index_phone_column] != '':
                phone = item[index_phone_column]
                if 'доб.' in phone:
                    pattern = r"(\+7|8)?[\s-]*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?доб\.\s*(\d+)\)?"
                    sub_pattern = r"+7(\2)\3-\4-\5 доб.\6"
                else:
                    pattern = r"(\+7|8)?[\s-]*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
                    sub_pattern = r"+7(\2)\3-\4-\5"
                contacts_list[i][index_phone_column] = re.sub(pattern, sub_pattern, phone)

    return contacts_list