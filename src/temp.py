fridge = {
    "долгопортищиеся": {
        "консервы": ["Лосось", "килька"],
        "мёд": ["Пчёлка", "Сытый медведь"]
    },
    "скоропортищиеся": {
        "кисломолочные": ["Молоко", "Творог"],
        "мясное": ["копчёнка", "Курица"]
        }
}   
print(fridge)

def add_item(data):
    if not data:
        print("Сначала создайте хотя бы одну категорию.")
        return
    
    print("\nДоступные категории:")

    categories = list(data.keys())
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")







add_item(fridge)