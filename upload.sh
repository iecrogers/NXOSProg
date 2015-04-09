#!/bin/bash
read -p "Enter Git update comment: " comment
commit="commit -m"
git add .
git status
git $commit "$comment"
git push -u origin master