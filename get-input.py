import requests

day = int(input('Day: '))
session_id = open('.cookie').read().strip()
headers = {'Cookie': 'session={}'.format(session_id)}
r = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day),
                 headers=headers)
open('day-{}/input.txt'.format(day), 'w').write(r.text)
