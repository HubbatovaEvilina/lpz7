class Store:
    def __init__(self):
        self.categories = {
            'электроника': {
                'ноутбук': {'цена': 75000, 'количество': 5},
                'наушники': {'цена': 3000, 'количество': 12},
                'монитор': {'цена': 18000, 'количество': 4}
            },
            'книги': {
                'javascript': {'цена': 1200, 'количество': 8},
                'гарри поттер': {'цена': 800, 'количество': 3},
                '1984': {'цена': 600, 'количество': 6}
            },
            'одежда': {
                'футболка': {'цена': 1500, 'количество': 10},
                'джинсы': {'цена': 3500, 'количество': 4},
                'кроссовки': {'цена': 5500, 'количество': 2}
            }
        }

    def show_category(self, category):
        if category in self.categories:
            for product, data in self.categories[category].items():
                print(f"{product}: {data['цена']} руб. (остаток: {data['количество']})")
        else:
            print("Категория не найдена")

    def buy_product(self, category, product, quantity):
        if category in self.categories and product in self.categories[category]:
            if self.categories[category][product]['количество'] >= quantity:
                self.categories[category][product]['количество'] -= quantity
                print(f"Куплено {quantity} шт. товара {product}")
            else:
                print("Недостаточно товара")
        else:
            print("Товар или категория не найдены")

    def total_value(self):
        total = 0
        for category in self.categories.values():
            for product in category.values():
                total += product['цена'] * product['количество']
        return total


words = ['яблоко', 'груша', 'апельсин', 'банан']
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

keys = ['id', 'name', 'price']
values = [1, 'телефон', 15000]
dict_from_lists = dict(zip(keys, values))
print(dict_from_lists)

text = "генераторы словарей"
char_freq = {}
for char in text:
    if char != ' ':
        char_freq[char] = char_freq.get(char, 0) + 1
print(char_freq)

inverted_freq = {}
for char, count in char_freq.items():
    if count not in inverted_freq:
        inverted_freq[count] = []
    inverted_freq[count].append(char)
print(inverted_freq)

store = Store()
store.show_category('электроника')
store.buy_product('электроника', 'ноутбук', 2)
print(store.total_value())