def legendary_farming():
    legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
    junks = {}
    while True:
        items = input().lower()
        items = items.split(' ')
        for value, material in zip(items[0::2], items[1::2]):
            value = int(value)
            if material in ['shards', 'fragments', 'motes']:
                legendary_items[material] += value
                if legendary_items[material] >= 250:
                    legendary_items[material] -= 250
                    special_item = ''
                    if material == 'shards':
                        special_item = 'Shadowmourne'
                    elif material == 'fragments':
                        special_item = 'Valanyr'
                    elif material == 'motes':
                        special_item = 'Dragonwrath'
                    print_legendary_items(legendary_items, junks, special_item)
                    return
            else:
                if material in junks.keys():
                    junks[material] += value
                else:
                    junks[material] = value


def print_legendary_items(legendary_items, junks, special_item):
    print(f'{special_item} obtained!')
    for material, value in legendary_items.items():
        print(f'{material}: {value}')
    for material, value in junks.items():
        print(f'{material}: {value}')


legendary_farming()
