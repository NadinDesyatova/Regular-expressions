def filling_dict(contacts_list, contacts_dicts):
    for i, item in enumerate(contacts_list):
        if i > 0:
            for key in contacts_dicts:
                if key == " ".join(item[:2]):
                    for column_name, column_value in zip(contacts_list[0], item):
                        if column_value != '':
                            contacts_dicts[key][column_name] = column_value

    return contacts_dicts