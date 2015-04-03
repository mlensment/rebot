#!/bin/bash

git add .
git commit -m "Update"
git push origin master && ssh pi@192.168.0.18 'cd ~/projects/rebot && git pull origin master'
