# pyydnspod
Pyydnspod is a single file dnspod.cn api manipulator.

You can easily update your server's dns records automatically. Please setup your records on web console of https://www.dnspod.cn/ firstly.

replace the code
``` python
user_email='Your username to login dnspod.cn'
user_password='your password'
user_domain ='your Domain name'
user_subdomain=['@','www'] #input your subdomain as list
```
at the beginning of .py file with your own setting.

And run as 
``` bash
python2 pyydnspod.py
```

It gets public ip addresses automatically, supports both ipv4 and ipv6.
