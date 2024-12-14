#!/usr/bin/bash

if [ ! -f env.sh ]; then
    echo "env.sh not found"
    exit 1
fi

source env.sh

git add code-2.py && git commit -m "update code for 2024/d$DAY_N"
