word = input("Enter a word: ")

letter_indexes = {}
for index, letter in enumerate(word):
    if letter not in letter_indexes:
        letter_indexes[letter] = []
    letter_indexes[letter].append(index)

print(letter_indexes)


items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

money_in_wallet = int(''.join(filter(str.isdigit, wallet)))
affordable_items = []

for item, price in items_purchase.items():
    item_price = int(''.join(filter(str.isdigit, price)))
    if item_price <= money_in_wallet:
        affordable_items.append(item)

if affordable_items:
    affordable_items.sort()
    print(affordable_items)
else:
    print("Nothing")
