#!/bin/bash

rm index.html
# run the following in original folder
# jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10
cp -i ../tech/$1.ipynb $1.ipynb
cp -i ../tech/folium* .
cp -i ../tech/bokeh* .
cp -i ../tech/times.png .
jupyter-nbconvert --to slides $1.ipynb --reveal-prefix=reveal.js

mv $1.slides.html index.html
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
