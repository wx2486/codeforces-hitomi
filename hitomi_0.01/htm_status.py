#! /usr/bin/python3

# codeforces hitomi project
#
# wx2486, 2014-7-5
#
# one contest's status update/refresh all/import from file
# get status by user handle if api is not contest.status
#
# functions:
#
# update: get new status
# refresh all: get all status
# import from file: used when recreating database table

import json
import urllib.request
import mysql.connector

# function get_status
# modes: 'update', 'refresh', 'import', 'dump'

def get_status(id, mode='update', api='contest.status'):
    print(mode+' '+api+' '+str(id))
    target_url = None
    file_dir = None
    if api == 'contest.status':
        target_url = 'http://codeforces.com/api/contest.status?'\
            'contestId='+str(id)
        file_dir = 'contest_status/'
    else:
        target_url = 'http://codeforces.com/api/user.status?'\
            'handle='+str(id)
        file_dir = 'user_status/'
    target_url_from = 1 
    file_path = '/var/hitomi/'
    file_name = str(id)+'.dat'

    if mode == 'import':
        json_target = json.load(open(file_path+file_dir+file_name, 'r'))
        status_to_mysql(json_target['result'])
        return

    file_content = None
    if mode == 'update':
        try:
            target_url_from = len(json.load(open(file_path+file_dir+file_name, 'r'))['result']) + 1
        except Exception as ex:
            print("Error: can't open data file: "+str(ex))
            target_url_from = 1
            mode = 'refresh'

    target_url += '&from='+str(target_url_from)
    target = urllib.request.urlopen(target_url).read().decode()

    if mode == 'dump' or mode == 'refresh':
        dump_file = open(file_path+file_dir+file_name, 'w')
        dump_file.write(target)
        dump_file.close()
        if (mode == 'dump'):
            return

    json_target = json.loads(target)

    if json_target['status'] != 'OK':
        print('Response status not OK.')
        return

    status_to_mysql(json_target['result'])

def status_to_mysql(subms):
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

    mysql_con = mysql.connector.connect(user='hitomi',
                                        password='sharingan',
                                        database='codeforces_hitomi')
    mysql_cursor = mysql_con.cursor()

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

    mysql_cursor.close()
    mysql_con.close()
            
    return
