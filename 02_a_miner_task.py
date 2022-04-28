def miner_task():
    resources = {}
    while True:
        resource = input()
        if resource == 'stop':
            break
        quantity = int(input())
        if resource not in resources:
            resources[resource] = 0
        resources[resource] += quantity

    for key, value in resources.items():
        print(f'{key} -> {value}')


miner_task()
