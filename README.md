# pyydnspod
Pyydnspod is a single file dnspod.cn api manipulator, it supports both **ipv4 and ipv6**.

You can easily update your server's dns records automatically when your server's ip is changed. But please **setup your records on web console of https://www.dnspod.cn/  before you use it first time**.

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
