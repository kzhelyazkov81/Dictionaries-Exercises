def phonebook_info():
    phonebook = {}
    condition = False
    while True:
        data = input()
        if data.isdigit():
            condition = contact_info(int(data), phonebook)
        else:
            data = data.split('-')
            contact = data[0]
            number = data[1]
            phonebook[contact] = number
        if condition:
            break


def contact_info(data, phonebook):
    for i in range(data):
        contact_name = input()
        if contact_name in phonebook:
            contact_number = phonebook[contact_name]
            print(f'{contact_name} -> {contact_number}')
        else:
            print(f'Contact {contact_name} does not exist.')
    condition = True
    return condition


phonebook_info()
