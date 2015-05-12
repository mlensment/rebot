#!/bin/bash

export LD_PRELOAD=/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so
if [ -z "$@" ]; then
  python rebot.py
else
  python rebot.py "$@"
fi
