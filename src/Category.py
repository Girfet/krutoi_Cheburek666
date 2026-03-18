def _print_nested(value, indent=2):
    """Рекурсивно печатает списки и словари с красивыми отступами."""
    spaces = " " * indent

    if isinstance(value, list):
        if value:
            for i, item in enumerate(value, start=1):
                print(f"{spaces}{i}. {item}")
        else:
            print(f"{spaces}(пусто)")
        return

    if isinstance(value, dict):
        if not value:
            print(f"{spaces}(пусто)")
            return

        for key, nested in value.items():
            print(f"{spaces}- {key}:")
            _print_nested(nested, indent + 4)
        return

    print(f"{spaces}{value}")


def show_all(data):
    """Показать все категории, включая холодильник с подкатегориями."""
    if not data:
        print("\nСписок пуст.\n")
        return

    print("\n" + "=" * 50)

    for key, value in data.items():
        print(f"\n{key}:")
        _print_nested(value, indent=2)

    print("\n" + "=" * 50 + "\n")


def add_category(data):
    """Добавить обычную категорию (верхнего уровня)."""
    name = input("Введите название категории: ").strip()
    if name == "":
        print("Название не может быть пустым.")
        return
    if name in data:
        print(f"Категория '{name}' уже существует.")
        return

    data[name] = []  # обычная категория хранит список
    print(f"Категория '{name}' добавлена!")


def add_item_to_simple_category(data):
    """Добавить элемент в обычную категорию (где значение — список)."""
    simple = []
    for k in data:
        if isinstance(data[k], list):
            simple.append(k)

    if not simple:
        print("Нет обычных категорий. Сначала добавьте категорию (например 'Животные').")
        return

    print("\nОбычные категории:")
    for i in range(len(simple)):
        print(f"  {i + 1}. {simple[i]}")

    choice = input("Выберите номер категории: ").strip()
    if not choice.isdigit():
        print("Неверный ввод.")
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(simple):
        print("Неверный номер.")
        return

    cat = simple[idx]
    item = input(f"Введите элемент для '{cat}': ").strip()
    if item == "":
        print("Элемент не может быть пустым.")
        return
    if item in data[cat]:
        print(f"'{item}' уже есть в '{cat}'.")
        return

    data[cat].append(item)
    print(f"'{item}' добавлен в '{cat}'!")


def add_item_to_fridge(data):
    """Добавить продукт в холодильник -> подкатегорию."""
    if "Холодильник" not in data or not isinstance(data["Холодильник"], dict):
        print("Категории 'Холодильник' нет. Сначала создайте её (пункт меню 'Создать холодильник').")
        return

    fridge = data["Холодильник"]
    subcats = list(fridge.keys())

    print("\nПодкатегории в 'Холодильник':")       #тута чё та надо будет поменять
    for i in range(len(subcats)):
        print(f"  {i + 1}. {subcats[i]}")         

    choice = input("Выберите номер подкатегории: ").strip()   # ну и в целом
    if not choice.isdigit():
        print("Неверный ввод.")
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(subcats):
        print("Неверный номер.")
        return

    sub = subcats[idx]
    target = fridge[sub]

    selected_path = ["Холодильник", sub]

    if isinstance(target, dict):
        inner_subcats = list(target.keys())
        if not inner_subcats:
            print("В выбранной подкатегории пока нет групп для добавления.")
            return

        print(f"\nГруппы в '{sub}':")
        for i in range(len(inner_subcats)):
            print(f"  {i + 1}. {inner_subcats[i]}")

        inner_choice = input("Выберите номер группы: ").strip()
        if not inner_choice.isdigit():
            print("Неверный ввод.")
            return

        inner_idx = int(inner_choice) - 1
        if inner_idx < 0 or inner_idx >= len(inner_subcats):
            print("Неверный номер.")
            return

        inner_sub = inner_subcats[inner_idx]
        target = target[inner_sub]
        selected_path.append(inner_sub)

    if not isinstance(target, list):
        print("Неподдерживаемый формат данных в 'Холодильник'.")
        return

    product = input(f"Введите продукт для '{selected_path[-1]}': ").strip()

    if product == "":
        print("Продукт не может быть пустым.")
        return

    if product in target:
        print(f"'{product}' уже есть в '{selected_path[-1]}'.")
        return

    target.append(product)
    print(f"'{product}' добавлен в '{' -> '.join(selected_path)}'!")


def create_fridge_with_defaults(data):
    """
    Создаёт категорию 'Холодильник' с двумя подкатегориями
    и добавляет туда пример продуктов.
    """
    data["Холодильник"] = {
        "долгопортищиеся": {
            "консервы": ["Лосось", "килька"],
            "мёд": ["Пчёлка", "Сытый медведь"]
        },
        "скоропортищиеся": {
            "кисломолочные": ["Молоко", "Творог"],
            "мясное": ["копчёнка", "Курица"]
            }
    }
        


def main():
    # Стартовые данные: как раньше + (холодильник создаётся по кнопке, либо можно сразу)
    data = {
        "Животные": ["Лев", "Слон", "Черепаха"],
        "Овощи": ["Морковь", "Картофель"],
        "Техника": ["Ноутбук", "Телефон"]
    }

    while True:
        print("=== МЕНЮ ===")
        print("1. Показать всё")
        print("2. Добавить обычную категорию")
        print("3. Добавить элемент в обычную категорию")
        print("4. Создать 'Холодильник' (с подкатегориями и примерами)")
        print("5. Добавить продукт в 'Холодильник'")
        print("0. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            show_all(data)
        elif choice == "2":
            add_category(data)
        elif choice == "3":
            add_item_to_simple_category(data)
        elif choice == "4":
            create_fridge_with_defaults(data)
        elif choice == "5":
            add_item_to_fridge(data)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")


main()