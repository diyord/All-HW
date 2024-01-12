students_data = {}

def add_student():
    student_id = input("Введите идентификационный номер ученика: ")
    name = input("Введите имя ученика: ")
    grade = input("Введите класс ученика: ")

    students_data[student_id] = {
        'Имя': name,
        'Класс': grade
    }

    print(f"Ученик {name} успешно добавлен!")

def view_student():
    student_id = input("Введите идентификационный номер ученика: ")

    if student_id in students_data:
        student_info = students_data[student_id]
        print(f"Имя: {student_info['Имя']}")
        print(f"Класс: {student_info['Класс']}")
    else:
        print("Ученик с таким идентификационным номером не найден.")

def main():
    while True:
        print("\n1. Добавить ученика")
        print("2. Просмотреть информацию об ученике")
        print("3. Выйти")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            add_student()
            #print(students_data)
        elif choice == '2':
            view_student()
            #print(students_data)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()