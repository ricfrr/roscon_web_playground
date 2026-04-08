#!/bin/bash

if [ $(git status --porcelain | wc -l) -ne "0" ]; then
  git status
  echo ""
  echo "ERROR: Local changes detected. >> Please make sure you don't have any local changes before building and uploading."
  exit 1
fi

if [ -d 2023 ]
then
  rsync -ave ssh --delete 20xx username@example.com:/var/www/rosconxx.org/ --exclude prospectus --delete-excluded --verbose
else
  echo "No directory 20xx, did you build it first?"
fi
