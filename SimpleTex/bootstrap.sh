#!/bin/sh
export FLASK_APP=./SimpleTex_scripts/test.py
python3 -m pipenv run flask --debug run -h 0.0.0.0