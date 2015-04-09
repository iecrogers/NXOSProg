#!/bin/bash
read -p "Enter Git update comment: " comment
#gitadd = "git add ."
git add "."
git status
git "commit" "-m" $comment
git "push" "-u" "origin" "master"