#!/bin/bash -xv

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
now=$(date +%H%M%S)
now=$((now - 2))

cat /tmp/mypkg.log |
grep "${now}"
