def register(name, plate):
    if name in registered_users.keys():
        print(f'ERROR: already registered with plate number {plate}')
    else:
        registered_users[name] = plate
        print(f'{name} registered {plate} successfully')


def unregister(name):
    if name not in registered_users:
        print(f'ERROR: user {name} not found')
    else:
        del registered_users[name]
        print(f'{name} unregistered successfully')


def print_registered():
    for user in registered_users.keys():
        print(f'{user} => {registered_users[user]}')


n = int(input())
registered_users = {}
for i in range(n):
    command = input().split(' ')
    action = command[0]
    username = command[1]
    if action == 'register':
        license_plate_number = command[2]
        register(username, license_plate_number)
    elif action == 'unregister':
        unregister(username)
print_registered()
