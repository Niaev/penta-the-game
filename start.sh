#!/bin/bash

export $(grep -v '^#' .env | xargs)

fuser -k -n tcp $PORT
cd $CWDIR

source ./venv/bin/activate
exec nohup uwsgi -w index:app --logto app.log --http $HOST:$PORT > app.out &