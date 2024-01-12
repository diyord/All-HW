contact = ['Amir', 'Akbar', 'Hitler']
while True:
    a = int(input('1-add, 2-delete, 3-change: '))

    if a ==1:
        new_contact = input('Write name contact which you want to added: ')
        contact.append(new_contact)
        print(f'The {new_contact} was successfully added!')
        print(contact)
    elif a ==2:
        old_contact = input('Write name contact which you want to delete: ')
        contact.remove(old_contact)
        print(f'The contact {old_contact} was successfully deleted!')
        print(contact)
    elif a ==3:
        old_name = input('Write name contact which you want to change: ')
        new_name = input('Write new name: ')
        if old_name in contact:
            index = contact.index(old_name)
            contact [index] = new_name
            print(f'The contact {new_name} was successfully changed!')
            print(contact)