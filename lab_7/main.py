import components.exponats.service as exponats
import components.workers.service as workers


# print(exponats.create_one({
#       "name": "Паладий",
#       "directors_id": [
#           1,
#           2
#       ],
# }))
#
#
# print(exponats.delete_one_by_id(4))

# print(exponats.get_all())

# print(exponats.get_one_by_id(1))

# print(exponats.update_one_by_id(4, {
#       "name": "Бриллиант",
#       "directors_id": [
#         1,
#         2
#       ],
#       }))

while True:
    print("Меню:")
    print("1. Создать работника")
    print("11. Создать экспонат")
    print("2. Получить список всех работников")
    print("22. Получить список всех экспанатов")
    print("3. Получить информацию о работнике по ID")
    print("33. Получить информацию о экспанате по ID")
    print("4. Обновить информацию о работнике по ID")
    print("44. Обновить информацию о экспанате по ID")
    print("5. Удалить работника по ID")
    print("55. Удалить экспонат по ID")

    choice = input("Выберите пункт меню (1-55): ")

    if choice == "1":
        name = input("Введите имя работника: ")
        salary = input("Введите зарплату: ")
        contacts_email = input("Введите email работника: ")
        contacts_phone = input("Введите телефон работника: ")

        result = workers.create_one({
            "name": name,
            "salary": salary,
            "contacts": {
                "email": contacts_email,
                "phone": contacts_phone
            }
        })

        print(result)
    elif choice == "11":
        name = input("Введите имя экспаната: ")
        directors_id = input("Введите ID начальника: ")

        directors_id = [str(id.strip()) for id in directors_id.split(",")] #даление лишних пробелы в начале и конце строки

        result = exponats.create_one({
            "name": name,
            "directors_id": directors_id,
        })

        print(result)

    elif choice == "2":
        result = workers.get_all()
        print(result)
    elif choice == "22":
        result = exponats.get_all()
        print(result)

    elif choice == "3":
        workers_id = input("Введите ID работника: ")
        result = workers.get_one_by_id(int(workers_id))
        print(result)
    elif choice == "33":
        customer_id = input("Введите ID экспаната': ")
        result = exponats.get_one_by_id(int(customer_id))
        print(result)

    elif choice == "4":
        workers_id = input("Введите ID работника: ")
        name = input("Введите новое имя работника: ")
        contacts_email = input("Введите новый email работника: ")
        contacts_phone = input("Введите новый телефон работника: ")

        result = workers.update_one_by_id(int(workers_id), {
            "name": name,
            "contacts": {
                "email": contacts_email,
                "phone": contacts_phone
            }
        })

        print(result)
    elif choice == "44":
        exponats_id = input("Введите ID экспоната: ")
        name = input("Введите новое имя экспоната: ")
        directors_id = input("Введите ID директора: ")

        result = exponats.update_one_by_id(int(exponats_id), {
            "name": name,
            "directors_id": directors_id
        })

        print(result)

    elif choice == "5":
        seller_id = input("Введите ID работника: ")
        result = workers.delete_one_by_id(int(seller_id))
        print(result)
    elif choice == "55":
        customer_id = input("Введите ID экспоната: ")
        result = exponats.delete_one_by_id(int(customer_id))
        print(result)


        break

    else:
        print("Неверный выбор. Попробуйте снова.")
