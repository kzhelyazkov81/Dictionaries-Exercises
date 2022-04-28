def add_employee(company, id):
    if company not in companies:
        companies[company] = [id]
    else:
        if id not in companies[company]:
            companies[company].append(id)


def print_companies():
    for company_name, employees in companies.items():
        print(f'{company_name}')
        for id in employees:
            print(f'-- {id}')


companies = {}
while True:
    data = input()
    if data == 'End':
        break
    data = data.split(' -> ')
    company_name = data[0]
    employee_id = data[1]
    add_employee(company_name, employee_id)
print_companies()
