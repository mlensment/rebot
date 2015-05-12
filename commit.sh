#!/bin/bash

git add --all
if [ -z "$1" ]; then
  git commit -m "Update"
else
  git commit -m "$1"
fi

git push origin master && ssh pi@192.168.1.152 'cd ~/projects/rebot && git pull origin master'
