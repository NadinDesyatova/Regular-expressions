from application.list.create_new_list import create_new_contacts_list
from application.list.filling_dict import filling_dict
from application.list.name_correct import name_correct
from application.list.phone_correct import phone_correct
from application.list.create_contacts_dict import create_contacts_dict


def list_conversion(contacts_list):
    list_with_correct_names = name_correct(contacts_list)

    contacts_dicts = create_contacts_dict(list_with_correct_names)

    list_with_correct_phones = phone_correct(list_with_correct_names, 5)

    full_contacts_dicts = filling_dict(list_with_correct_phones, contacts_dicts)

    new_contacts_list = create_new_contacts_list(full_contacts_dicts)

    return new_contacts_list