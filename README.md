# trayo
Small tray icon to switch between performance/powersave for intel_pstate.

![alt tag](https://raw.githubusercontent.com/kursion/trayo/master/screenshot.png)

# Installation permanent
* Run ./INSTALL.sh
* Install cpupower
* Add cpupower NOPASSWD option.
  `$ sudo visudo` and add
  `YOUR_USER_NAME ALL=NOPASSWD: /bin/cpupower`
* Add `trayo` to your .xinitrc
* Reboot or restart

# Usage
Nothing special just run `./INSTALL.sh` and launch it

`$ trayo`

# TESTED
Archlinux, i3WM on 2015-08-06
