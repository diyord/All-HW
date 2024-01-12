list_cont = ['ivan', 'sasha', 'pasha']

choice = int(input('1-add, 2-remove, 3-index: '))

if choice == 1:
    new_conatc = input('Write contact which you want to add: ')
    list_cont.append(new_conatc)
    print(f' Your contact {new_conatc} was successfully added!')

elif choice == 2:
    old_conatc = input('Write contact which you want to deleted: ')
    list_cont.remove(old_conatc)
    print(f'Your contact {old_conatc} was successfully deleted!')

elif choice == 3:
    old_name = input('Write contact which you want to change: ')
    new_name = input('Write a new contact: ')
    if old_name in list_cont:
        index = list_cont.index(old_name)
        list_cont[index] = new_name
        print(f'New contact {new_name} was successfully changed!')
else:
    print('contacts was not found in list')