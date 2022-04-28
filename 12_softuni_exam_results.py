def submit(username, language, points):
    if language not in submissions_count.keys():
        submissions_count[language] = 0
    submissions_count[language] += 1
    if language in submissions.keys():
        if username in submissions[language].keys():
            if points > submissions[language][username]:
                submissions[language][username] = points
        else:
            submissions[language][username] = points
    else:
        submissions[language] = {username: points}


def result():
    print('Results:')
    for language in submissions.keys():
        for username, points in submissions[language].items():
            if username not in banned:
                print(f'{username} | {points}')
    print('Submissions:')
    for language, user in submissions.items():
        print(f'{language} - {submissions_count[language]}')


submissions = {}
submissions_count = {}
banned = []
while True:
    data = input()
    if data == 'exam finished':
        break
    data = data.split('-')
    username = data[0]
    if data[1] == 'banned':
        banned.append(username)
    else:
        language = data[1]
        points = int(data[2])
        submit(username, language, points)

result()