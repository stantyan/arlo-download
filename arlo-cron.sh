#!/bin/bash
PATH=/home/arlo/anaconda3/bin
python /home/arlo/arlo/arlo-download.py
rclone move -v --transfers 12 --ignore-existing /home/arlo/arlo/library/ gd:/apps/arlo.netgear.com/library/2018/
echo "Arlo daily backup completed"
