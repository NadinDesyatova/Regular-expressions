def create_contacts_dict(contacts_list):
    contacts_dicts = {}

    for i, item in enumerate(contacts_list):
        if i > 0:
            full_name = contacts_list[i][:2]
            contacts_dicts.setdefault(" ".join(full_name), {
                'lastname': '',
                'firstname': '',
                'surname': '',
                'organization': '',
                'position': '',
                'phone': '',
                'email': ''
            })

    return contacts_dicts