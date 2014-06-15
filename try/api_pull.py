#!/usr/bin/python3

# codeforces hitomi project
#
# wx2486, 2014-6-15
#
# try with python
#
# functions:
# pull data from codeforces.com
# save raw json data into raw.dat
# save data in table format into sub.dat

print('Eyes are open!')
 
import urllib.request
import json

#### configure
# edit this block to configure this script

# Id of the contest. It is not the round number. It can be seen in contest URL. For example: /contest/374/status
url_contestId = '374'

# 1-based index of the first submission to return.
url_from = '1'

# Number of returned submissions.
url_count = '10'

# Should I print data on the screen? True or False
print_target = True

#
#### end of configure

print('Mission confirmed.')

target_url = 'http://codeforces.com/api/contest.status?contestId=' + url_contestId + '&from=' + url_from + '&count=' + url_count

print('Link start.')
print('Target url: ' + target_url)
print('Downloading...')

target = urllib.request.urlopen(target_url).read().decode()

print('Target obtained.')
print('Dumping target as it is...')

raw_file = open('raw.dat', 'w')
raw_file.write(target)
raw_file.close()

print('Done.')

if print_target:
    print('Target:')
    print(json.dumps(target, sort_keys=True, indent=4))

dic = json.loads(target)

if dic['status'] != 'OK':
    print('response status not ok')
    exit()

subs = dic['result']
#print(type(subs))
print(str(len(subs)) + ' submissions:')

for i in subs[0]:
    print(i + '\t', end='')
print('')

for i in subs:
    for j in i:
        if j == 'problem':
            print(i['problem']['index'] + '\t', end='')
        elif j == 'author':
            print(i['author']['members'][0]['handle'] + '\t', end='')
        else:
            print(str(i[j]) + '\t', end='')
    print('')
