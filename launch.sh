#!/bin/bash
export LD_PRELOAD=/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so
if [ -z "$1" ]; then
  python rebot.py --frame $1
else
  python rebot.py
fi
