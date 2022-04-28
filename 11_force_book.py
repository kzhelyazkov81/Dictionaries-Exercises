def add_user(name, new_side):
    condition = [current_side for current_side in force_sides if name in force_sides[current_side]]
    if len(condition) == 0:
        if new_side in force_sides.keys():
            force_sides[new_side].append(name)
        else:
            force_sides[new_side] = [name]


def change_side(name, new_side):
    exist = False
    for force_side, names in force_sides.items():
        if name in names:
            exist = True
            force_sides[force_side].remove(name)
            if new_side in force_sides.keys():
                force_sides[new_side].append(name)
            else:
                force_sides[new_side] = [name]
            break
    if not exist:
        if new_side in force_sides.keys():
            force_sides[new_side].append(name)
        else:
            force_sides[new_side] = [name]
    print(f"{name} joins the {new_side} side!")


def print_users():
    for force_side, users in force_sides.items():
        members = len(force_sides[force_side])
        if members != 0:
            print(f'Side: {force_side}, Members: {members}')
            for force_user in users:
                print(f'! {force_user}')


force_sides = {}
while True:
    data = input()
    if data == 'Lumpawaroo':
        break
    if "|" in data:
        command = data.split(' | ')
        side = command[0]
        user = command[1]
        add_user(user, side)
    elif "->" in data:
        command = data.split(' -> ')
        side = command[1]
        user = command[0]
        change_side(user, side)
print_users()