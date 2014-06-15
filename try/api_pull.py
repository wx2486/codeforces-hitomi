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
url_contestId = '374'

# 1-based index of the first submission to return.
url_from = '1'

# Number of returned submissions.
url_count = '10'

# Should I print data on the screen? True or False
print_target = False

#
#### end of configure

print('Mission confirmed.')

target_url = 'http://codeforces.com/api/contest.status?contestId=' + url_contestId + '&from=' + url_from + '&count=' + url_count

print('Link start.')
print('Target url: ' + target_url)
print('Downloading...')

target = urllib.request.urlopen(target_url)

print('Target obtained.')
print('Transform target into nice json format...')

json_target = json.dumps(json.loads(target.read().decode()),sort_keys=True, indent=4)

print('Done.')

if (print_target):
    print('Target:')
    print(json_target)

print('Dumping target in nice json format...')

raw_file = open('json.dat', 'w')
raw_file.write(json_target)
raw_file.close()

print('Done.')
print('Eyes closed.')
