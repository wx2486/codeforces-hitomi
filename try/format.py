#!/usr/bin/python3

# codeforces hitomi project
#
# wx2486, 2014-6-15
#
# try with python
#
# functions:
# read json from json.dat
# transform it into table format
# save it into table.dat

print('Eyes are open!')

import json

print('Eating hard disk...', end='', flush=True)

json_file = open('json.dat', 'r')

print('Done.')
print('Loading json...', end='', flush=True)

json_target = json.load(json_file)

print('Done.')

subms = json_target['result']

fields = ('id',
          'contestId',
          'creationTimeSeconds',
          'relativeTimeSeconds',
          'problem',
          'author',
          'programmingLanguage',
          'verdict',
          'testset',
          'passedTestCount',
          'timeConsumedMillis',
          'memoryConsumedBytes')

table = ''
for i in range(len(fields)):
    if i > 0:
        table += '\t'
    table += fields[i]
table += '\n'

print('Transform json into a table...', end='', flush=True)

for sub in subms:
    for i in range(len(fields)):
        if len(sub['author']['members']) != 1:  # ignore teams
            continue
        if i > 0:
            table += '\t'
        if fields[i] == 'problem':
            table += sub['problem']['index']
        elif fields[i] == 'author':
            table += sub['author']['members'][0]['handle']
        else:
            table += str(sub[fields[i]])
    table += '\n'

print('Done.')
print('Dump table...', end='', flush=True)

table_file = open('table.dat', 'w')
table_file.write(table)
table_file.close()

print('Done.')
print('Eyes closed.')
