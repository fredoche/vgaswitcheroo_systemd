#! /bin/sh
service=$(/bin/ls *.service)
echo "Do you want to enable the $service? y/n"
read flag

if [[ flag -eq "y" ]]; then
    cp -i "$service" "/usr/lib/systemd/system/"
    systemctl enable $service &&
    echo "$service successfully installed and enabled."
fi

echo "Should we load the radeon module during bootup? y/n"
read bootup
if [[ bootup -eq "y" ]]; then
    echo radeon > /etc/modules-load.d/radeon.conf &&
    echo "The 'radeon' module is now loaded during startup. See /etc/modules-load.d/radeon.conf"
fi

echo "Should we load the radeon module during bootup? y/n"
read blacklist
if [[ blacklist -eq "y" ]]; then
    echo "blacklist radeon" >> /etc/modprobe.d/blacklist.conf &&
    echo "Added the radeon module to the blacklist in /etc/modprobe.d/blacklist.conf"
fi
