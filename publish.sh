#!/bin/bash

rm ./technology\ review/index.html
# run the following in original folder
# jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10
cp -i ../tech/$1.ipynb ./technology\ review/$1.ipynb
cp -i ../tech/folium_*.html ./technology\ review/plots
cp -i ../tech/bokeh_*.html ./technology\ review/plots
cp -i ../tech/times.png ./technology\ review/plots
jupyter-nbconvert --to slides ./technology\ review/$1.ipynb --reveal-prefix=reveal.js

mv ./technology\ review/$1.slides.html ./technology\ review/index.html
mkdir -p /tmp/workspace
cp -r * /tmp/workspace/
git add -A .
git commit -m "Update new"
git checkout -B gh-pages
cp -r /tmp/workspace/* .
git add -A .
git commit -m "new version"
git push origin master gh-pages
git checkout master
rm -rf /tmp/workspace
