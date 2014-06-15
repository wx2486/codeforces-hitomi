#!/usr/bin/python3

# codeforces hitomi project
#
# wx2486, 2014-6-15
#
# try with python
#
# functions:
# read json from json.dat
# send data to mysql

print('Eyes are open!')

import json
import mysql.connector

print('Eating hard disk...')

json_file = open('json.dat', 'r')

print('Done.')
print('Loading json...')

json_target = json.load(json_file)

print('Done.')

subms = json_target['result']

print('Focus on content.')

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

sql_head = 'insert ignore into submission ('

for i in range(len(fields)):
    if i > 0:
        sql_head += ', '
    sql_head += fields[i]

sql_head += ') values ('

print('Connect to the ocean...')

mysql_con = mysql.connector.connect(user='hitomi',
                                    password='sharingan',
                                    database='codeforces_hitomi')
mysql_cursor = mysql_con.cursor()

print('Done.')

print('Json flowing into the ocean...')

for sub in subms:
    sql_query = sql_head
    for i in range(len(fields)):
        if len(sub['author']['members']) != 1:  # ignore teams
            break

        if i > 0:
            sql_query += ', '

        if fields[i] == 'problem':
            sql_query += "'" + sub['problem']['index'] + "'"

        elif fields[i] == 'author':
            sql_query += "'" + sub['author']['members'][0]['handle'] + "'"

        elif fields[i] == 'programmingLanguage'\
                or fields[i] == 'verdict'\
                or fields[i] == 'testset':
            sql_query += "'" + sub[fields[i]] + "'"

        else:
            sql_query += str(sub[fields[i]])
    else:
        sql_query += ')'
        mysql_cursor.execute(sql_query)

mysql_con.commit()

print('Done.')
print('Eyes closed.')
