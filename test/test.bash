#!/bin/bash -xv

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
timejp=$(TZ='Asia/Tokyo' date +%H%M%S)
timejp=$((timejp-2))

cat /tmp/mypkg.log |
grep "${timejp}"
