#! /bin/sh
service=$(/bin/ls *.service)
echo "Do you want to enable the $service? y/n"
read flag
echo $enable
if [[ flag -eq "y" ]]; then
    systemctl enable $(pwd)/$service
    echo "$service successfully installed and enabled."
fi
