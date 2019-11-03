#!/bin/bash

cp -i ../tech/$1 $1
cp -i ../tech/$2 $2
jupyter-nbconvert --to slides $1 --reveal-prefix=reveal.js --SlidesExporter.reveal_scroll=True
mv slides.slides.html index.html
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
