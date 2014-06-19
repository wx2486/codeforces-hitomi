#!/bin/bash

id=0
startId=100436
endId=100460

for (( id=startId; id<endId; id=id+1));
do
    sed "s/^url_contestId = 1$/url_contestId = $id/" api_pull.py > api_pull_i.py;
    chmod 744 api_pull_i.py;
    ./api_pull_i.py;
#    ./mysql_push.py;
    mv json.dat json$id.dat
    echo Completed: $((id-startId+1)) of $((endId-startId))
done
