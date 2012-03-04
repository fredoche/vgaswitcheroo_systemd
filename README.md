vgaswitcheroo_systemd
=====================

You just bought a shiny new laptop with dual graphics adapter, and want to use a Linux distro with it. Luckily, you can use the vgaswitcheroo kernel module to manage the power issues, however you'd like to save power and save yourself trouble by automatically disabling the discrete adapter on startup. If your distribution uses systemd as init daemon, you can use these pretty simple files to solve this problem. As you might guess, I only tried this on a Fedora 16 distribution.
I will happily accept pull requests if anyone knows a better way to achieve the same results (ie. the Right Way To Do Things). If you also know how to make rpms for fedora, I'll gladly add it to this repository.

Description
===========

This project consists of two files: A systemd service definition file, and a simple shell script which will issue the right command to turn the graphic adapter OFF.

Installation
============

After cloning, move nodis.sh to the /root directory, and vgaswitcheroo.service to /lib/systemd/system/ . After that, issue the following command as root to enable the service on startup.
```# systemctl enable plop.service```

Usage
=====

This should be enough. If you need to check whether it's working or not, you can run, as root:
```cat /sys/kernel/debug/vgaswitcheroo/switch```
The expected output should show that the DIScrete adapter is off.
```
0:DIS: :Off:0000:01:00.0
1:IGD:+:Pwr:0000:00:02.0
```


