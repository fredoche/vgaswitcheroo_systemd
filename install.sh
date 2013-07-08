#! /bin/sh
service=$(/bin/ls *.service)

read -p "Do you want to enable the $service? y/n: "
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cp -i "$service" "/usr/lib/systemd/system/"
    systemctl enable $service
    echo "$service successfully installed and enabled."
fi

read -p "Should we load the radeon module during bootup? y/n: "
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo radeon > /etc/modules-load.d/radeon.conf
    echo "The 'radeon' module is now loaded during startup. See /etc/modules-load.d/radeon.conf"
fi

read -p "Should we load the radeon module during bootup? y/n: "
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "blacklist radeon" >> /etc/modprobe.d/blacklist.conf
    echo "Added the radeon module to the blacklist in /etc/modprobe.d/blacklist.conf"
fi
