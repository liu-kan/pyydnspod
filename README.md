# pyydnspod
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fliu-kan%2Fpyydnspod.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fliu-kan%2Fpyydnspod?ref=badge_shield)

Pyydnspod is a single file **dnspod.cn** and **name.com** api manipulator, it supports both **ipv4 and ipv6**.

You can easily update your server's dns records automatically when your server's ip is changed. But please **setup your records on web console of https://www.dnspod.cn/ or https://name.com before you use it first time**.

replace the code
``` python
tid='Your token ID'
token='Your Token'
user_domain ='Your domain'
user_subdomain=['@','www'] #input your subdomain as list
```
at the beginning of .py file with your own setting.

And run as 
``` bash
python2 pyydnspod.py
```

Add it to your startup script like rc.local or similar. If your ip will change from time to time when your server is running, add it to cron job by 
``` bash
crontab -e
```

It gets public ip addresses automatically, supports both ipv4 and ipv6.


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fliu-kan%2Fpyydnspod.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fliu-kan%2Fpyydnspod?ref=badge_large)