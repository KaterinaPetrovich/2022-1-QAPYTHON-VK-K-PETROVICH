#!/bin/bash

cd code || exit 1

pytest -s -l -v -n 2 --alluredir=/tmp/allure/