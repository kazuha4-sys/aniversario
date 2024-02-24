import datetime

def load_birthdays(filename):
    try:
        with open(filename, 'r') as file:
            birthdays = {}
            for line in file:
                name, date_str = line.strip().split(',')
                date = datetime.datetime.strptime(date_str, '%d/%m/%Y')
                birthdays[name] = date
            return birthdays
    except FileNotFoundError:
        return {}

def save_birthdays(birthdays, filename):
    with open(filename, 'w') as file:
        for name, date in birthdays.items():
            date_str = date.strftime('%d/%m/%Y')
            file.write(f"{name},{date_str}\n")

def add_birthday(name, date, birthdays, filename):
    birthdays[name] = date
    save_birthdays(birthdays, filename)

def get_birthdays_by_date(date, birthdays):
    return [name for name, bdate in birthdays.items() if bdate.day == date.day and bdate.month == date.month]

def check_birthdays_today(birthdays):
    today = datetime.datetime.now().date()
    today_birthdays = get_birthdays_by_date(today, birthdays)
    return today_birthdays

def main():
    filename = 'birthdays.txt'
    birthdays = load_birthdays(filename)
    
    today_birthdays = check_birthdays_today(birthdays)
    if today_birthdays:
        print(f"Aniversariantes de hoje ({datetime.datetime.now().date().strftime('%d/%m')}):")
        for name in today_birthdays:
            print(f"- {name}")
    else:
        print("Nenhum aniversariante hoje.")

    while True:
        print("\nMenu:")
        print("1. Adicionar aniversário")
        print("2. Ver todos os aniversariantes")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome da pessoa: ")
            date_str = input("Data de nascimento (dd/mm/aaaa): ")
            date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
            add_birthday(name, date, birthdays, filename)
        elif choice == '2':
            print("\nAniversariantes:")
            if birthdays:
                for name, bdate in birthdays.items():
                    print(f"{name}: {bdate.strftime('%d/%m/%Y')}")
            else:
                print("Nenhum aniversário cadastrado.")
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
