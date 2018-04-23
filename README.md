# arlo-download

Automation

::create a shell script::

sudo nano /home/arlo/arlo/arlo-cron.sh


:: and insert the following code::


#!/bin/bash
PATH=/home/arlo/anaconda3/bin
python /home/arlo/arlo/arlo.py
rclone move -v --transfers 12 --ignore-existing /home/arlo/arlo/library/ gd:/apps/arlo.netgear.com/library/2018/
echo "Arlo daily backup is completed"


::grant executable permissions::

sudo chmod +x /home/arlo/arlo/arlo-cron.sh


::edit cron jobs file::

sudo crontab -e


:: and insert the following job::

0 15 * * * /home/arlo/arlo/arlo-cron.sh
