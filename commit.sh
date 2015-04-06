#!/bin/bash

git add .
git commit -m "Update"
git push origin master && ssh pi@192.168.1.220 'cd ~/projects/rebot && git pull origin master'
