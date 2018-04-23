alias arlo_backup_dry = 'rclone move -v --transfers 12 --ignore-existing --dry-run /home/arlo/arlo/library/ gd:/apps/arlo.netgear.com/library/2018/'

alias arlo_backup = 'rclone move -v --transfers 12 --ignore-existing /home/arlo/arlo/library/ gd:/apps/arlo.netgear.com/library/2018/'
