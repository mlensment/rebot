#!/bin/bash

export LD_PRELOAD=/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so
python rebot.py $@
