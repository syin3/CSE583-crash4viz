#!/bin/bash

rm index.html
# run the following in original folder
# jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10
cp -i ../tech/$1.ipynb $1.ipynb
cp -i ../tech/$2 $2
jupyter-nbconvert --to slides $1 --reveal-prefix=reveal.js --SlidesExporter.reveal_scroll=True

mv $1.slides.html index.html
mkdir -p /tmp/workspace
cp -r * /tmp/workspace/
git add -A .
git commit -m "Update"
git checkout -B gh-pages
cp -r /tmp/workspace/* .
git add -A .
git commit -m "new version"
git push origin master gh-pages
git checkout master
rm -rf /tmp/workspace
