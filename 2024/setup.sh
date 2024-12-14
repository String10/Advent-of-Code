#!/usr/bin/bash

ROOT_DIR=$(realpath $(dirname "${BASH_SOURCE[0]}"))

WORK_DIR=$ROOT_DIR/day-$1
if [ ! -d $WORK_DIR ]; then
    mkdir $WORK_DIR
fi

pushd $WORK_DIR > /dev/null
touch puzzle.txt
cp $ROOT_DIR/template.py code-1.py
cp $ROOT_DIR/template.py code-2.py

# save for later commit message
echo "DAY_N=$1" > env.sh

echo "Finished setting up Day $1" && code code-1.py
