def create_new_contacts_list(contacts_dicts):
    new_contacts_list = [
        ['lastname',
         'firstname',
         'surname',
         'organization',
         'position',
         'phone',
         'email']
    ]

    for contact_name, value in contacts_dicts.items():
        contact = [
            value['lastname'],
            value['firstname'],
            value['surname'],
            value['organization'],
            value['position'],
            value['phone'],
            value['email']
        ]
        new_contacts_list.append(contact)

    return new_contacts_list