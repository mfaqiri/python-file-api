#!/bin/bash

if test -d venv; then
        rm -R venv
fi

mkdir venv

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
