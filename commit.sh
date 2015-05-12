#!/bin/bash

git add --all
if [ -z "$1" ]; then
  git commit -m "Update"
else
  git commit -m "$1"
fi

git push origin master && ssh pi@192.168.0.19 'cd ~/projects/rebot && git pull origin master'
