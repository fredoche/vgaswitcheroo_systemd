#! /bin/sh
service=$(/bin/ls *.service)
echo "Do you want to enable the $service? y/n"
read flag

if [[ flag -eq "y" ]]; then
    cp -i "$service" "/usr/lib/systemd/system/"
    systemctl enable $service
    echo "$service successfully installed and enabled."
fi
