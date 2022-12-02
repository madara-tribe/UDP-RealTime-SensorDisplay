#!/bin/sh
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -name '.DS_Store' -type f -ls -delete
mkdir -p bp bp/qtWidgets
cp *.py *.sh *.png bp/
cp qtWidgets/*.py bp/qtWidgets/
