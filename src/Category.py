def show_all(data):
    """Показать все категории, включая холодильник с подкатегориями."""
    if not data:
        print("\nСписок пуст.\n")
        return

    print("\n" + "=" * 50)

    for key in data:
        value = data[key]

        # Если значение — список, значит это "обычная" категория
        if isinstance(value, list):
            print(f"\n{key}:")
            if value:
                for i in range(len(value)):
                    print(f"  {i + 1}. {value[i]}")
            else:
                print("  (пусто)")

        # Если значение — словарь, значит это категория с подкатегориями (например холодильник)
        elif isinstance(value, dict):
            print(f"\n{key}:")
            subcats = value.keys()
            podsubcats = subcats.keys()
            for sub in podsubcats:
                items = value[sub]
                print(f"  - {sub}:")
                if items:
                    for i in range(len(items)):
                        print(f"      {i + 1}. {items[i]}")
                else:
                    print("      (пусто)")

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
    product = input(f"Введите продукт для '{sub}': ").strip()

    if product == "":
        print("Продукт не может быть пустым.")
        return

    if product in fridge[sub]:
        print(f"'{product}' уже есть в '{sub}'.")
        return

    fridge[sub].append(product)
    print(f"'{product}' добавлен в 'Холодильник' -> '{sub}'!")


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