from pprint import pprint
import csv
import re


def change_contacts(contacts):
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'

    for contact in contacts:
        full_name = contact[0] + contact[1] + contact[2]
        name_parts = re.sub(name_pattern, name_substitution, full_name).split()
        if len(name_parts) == 3:
            contact[0] = name_parts[0]
            contact[1] = name_parts[1]
            contact[2] = name_parts[2]
        if len(name_parts) == 2:
            contact[0] = name_parts[0]
            contact[1] = name_parts[1]
            contact[2] = ''
        if len(name_parts) == 1:
            contact[0] = name_parts[0]
            contact[1] = ''
            contact[2] = ''

    return contacts


def phone_change(contacts):
    phone_pattern = re.compile(r'(8|\+7)?\s*\(?(\d+)\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})\s*\(?(доб.)?\s?(\d+)?\)?')
    phone_substitution = r'+7(\2)\3-\4-\5 \6\7'

    for contact in contacts:
        contact[5] = phone_pattern.sub(phone_substitution, contact[5])

    return contacts


def duplicates():

    my_dict = {}

    for contacts in contacts_list[1:]:
        last_name = contacts[0]
        if last_name not in my_dict:
            my_dict[last_name] = contacts
        else:
            for id, item in enumerate(my_dict[last_name]):
                if item == '':
                    my_dict[last_name][id] = contacts[id]

    for last_name, contact in my_dict.items():
        for contacts in contact:
            if contact not in new_list:
                new_list.append(contact)
                
    return new_list


if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding="utf-8", newline='') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        new_list = []
        change_contacts(contacts_list)
        phone_change(contacts_list)
        duplicates()

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)
