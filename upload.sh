#!/bin/bash
read -p "Enter Git update comment: " comment
#find /users/Christopher/Documents/Customers/ -type f \
#-newermt $date -exec ls -l {} \; > /users/Christopher/Desktop/modified_Files.txt
#find /users/Christopher/Documents/Customers/ -type d -path "*/\.*" \
#-prune -o -not -name ".*" -type f -newermt $date -exec ls -l {} \; \
#> /users/Christopher/Desktop/modified_Files.txt
#find $pwd -not -iname $exclude -type f -newermt $date | xargs -r ls -lh \
#> /users/Christopher/Desktop/modified_Files.txt
git add .
git status
git commit -m $comment
git push -u origin master