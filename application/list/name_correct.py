import re


def name_correct(contacts_list):
    for i, item in enumerate(contacts_list):
        if i > 0:
            join_name = " ".join(item[:3])
            full_name_list = re.split("\s+", join_name)
            contacts_list[i][:3] = full_name_list[:3]

    return contacts_list