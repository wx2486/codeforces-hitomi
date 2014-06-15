#!/bin/bash

id=0
startId=1
endId=442

for (( id=startId; id<endId; id=id+1));
do
    echo complete $((id-startId)) of $((endId-startId))
    sed "s/^url_contestId = 1$/url_contestId = $id/" api_pull.py > api_pull_i.py;
    chmod 744 api_pull_i.py;
    echo pulling contest $id
    ./api_pull_i.py;
    echo pushing to mysql $id
    ./mysql_push.py;
    echo next to come
done
