#!/usr/bin/python3

# codeforces hitomi project
#
# wx2486, 2014-6-15
#
# try with python
#
# functions:
# pull data from codeforces.com
# save formatted json data into json.dat

print('Eyes are open!')
 
import urllib.request
import json

#### configure
# edit this block to configure this script

# Id of the contest. It is not the round number. It can be seen in contest URL. For example: /contest/374/status
url_contestId = 1

# 1-based index of the first submission to return. Ignored if less than 1
url_from = 0

# Number of returned submissions. ignored if less than 1
url_count = 0

# Should I print data on the screen? True or False
print_target = False

#
#### end of configure

print('Mission confirmed.')

target_url = 'http://codeforces.com/api/contest.status?contestId='\
    + str(url_contestId)
if url_from > 0:
    target_url += '&from=' + str(url_from)
if url_count > 0:
    target_url += '&count=' + str(url_count)

print('Link start.')
print('Target url: ' + target_url)
print('Downloading...')

target = urllib.request.urlopen(target_url)

print('Target obtained.')
print('Loading target...')

json_target = json.loads(target.read().decode())

print('Done.')
print('Checking server response status...')

if json_target['status'] != 'OK':
    print('Status: ' + json_target['status'])
    print('Comment: ' + json_target['comment'])
    print('Abort.')
    exit()

print('Status: OK')
print('Transform target into nice json format...')

json_target_str = json.dumps(json_target, sort_keys=True, indent=4)

print('Done.')

if (print_target):
    print('Target:')
    print(json_target_str)

print('Dumping target in nice json format...')

json_file = open('json.dat', 'w')
json_file.write(json_target_str)
json_file.close()

print('Done.')
print('Eyes closed.')
