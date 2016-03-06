# SRM Announcement Desktop Notifier
##### Never miss an important announcement of your college again :wink:

## Demo
![usage](/assets/usage.gif)

### How to run
```
$ git clone https://github.com/varundey/srmAnnouncementInformer.git
$ cd srmAnnouncementInformer/
$ python announcer.py
```

## Requirements
```
$ pip install beautifulsoup4
$ pip install requests
$ apt-get install python-gobject
$ apt-get install libnotify-bin
```

## Bonus :tada:
##### Coz who doesn't like some add-ons
The announcer.py file can be set under as a cron-job to be run at every minute/hour/boot. Alas the OSD of linux kernel and cronTab are set up under different environment, and thus we have to work our way around a bit. In order to create a cronjob for the python file, keep reading:
```
 chmod 700 srmAnnouncementInformer/bin/export_x_info
 sh srmAnnouncementInformer/bin/export_x_info
```
* Now open Dash and under Startup Applications, add the `export_x_info` script
* Under `crontab -e` add the following two lines in the begining
```
SHELL=/bin/bash
DISPLAY=:0.0
```
* Depending on your schedule and path, your crontab should look along the line of the following:
```
@reboot source ~/.Xdbus; python srmAnnouncementInformer/announcer.py
```

### Inspiration
This project was inspired from [Result-Reminder](https://github.com/Sandeeprds95/result-reminder) by [@Sandeeprds95](https://github.com/Sandeeprds95). Why not make a general announcement notifier. :smiley:

### Bug Hunt?
Report it at [issue tracker](https://github.com/varundey/srmAnnouncementInformer/issues) :gun: :bomb:

### License

MIT License http://varundey.mit-license.org/ © Varun Dey

