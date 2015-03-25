#!/bin/bash

git add .
git commit -m "Update"
ggpush && ssh pi@192.168.1.99 'cd ~/projects/rebot && git pull origin master'
