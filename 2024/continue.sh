#!/usr/bin/bash

ROOT_DIR=$(realpath $(dirname "${BASH_SOURCE[0]}"))

if [ ! -f code-1.py ]; then
    echo "code-1.py not found"
    exit 1
fi

git add code-1.py && cp code-1.py code-2.py

echo 'continue on Part 2' && code code-2.py
