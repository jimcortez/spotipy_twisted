#!/usr/bin/env bash

set -e

pip install coveralls python-subunit junitxml


python setup.py install
coverage run --include=*spotipy_twisted* tests/tests.py
#TODO  - for file in examples/*.py; do python $file; done

coverage xml -o coverage.xml
