#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
import urllib2
import json
import sys,re
import urllib
user_email='Your username to login dnspod.cn'
user_password='your password'
user_domain ='your Domain name'
user_subdomain=['@','www'] #input your subdomain as list

ip_add='http://www.zzsky.cn/code/ip/ip12.asp'
ip_add6='http://whatismyv6.com'

#user_subdomain为要设置的子域名，如www
ttl='120' #免费用户最低120
#ip_add='http://api.hostip.info/get_html.php'
#ip_add为获取ip的网址，该网址应该以最尽可能简洁的模式显示ip地址，
#不能连接国外网络的可以使用'http://www.zzsky.cn/code/ip/ip12.asp'
#也可以直接填入ip
#设置结束

pub_postdata={'login_email':user_email, 'login_password':user_password,'format':'json','lang':'en'}
user_agent_str='PyDdnsClient/1.1.1 (liukan@126.com)'
p_ip=re.compile(r'^http.*')
ip='127.0.0.1'
if p_ip.search(ip_add)==None:
    ip=ip_add
else:
    f = urllib2.urlopen(ip_add)
    re_ip=re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    ipr=re_ip.search(f.read())
    if ipr==None:
        print '无法自动获取ip，请确认连接正常或换用合适的获取ip地址，或手工输入ip'
        sys.exit()
    else:
        
        ip=ipr.group()
print 'ip:',ip

p_ip=re.compile(r'^http.*')
ip6='::1'
if p_ip.search(ip_add6)==None:
    ip6=ip_add6
else:
    f = urllib2.urlopen(ip_add6)
    re_ip6=re.compile('(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,4}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){,6}[0-9A-Fa-f]{1,4})?::)(?:%25(?:[A-Za-z0-9\\-._~]|%[0-9A-Fa-f]{2})+)?')
    ipv6str=f.read()
    #print ipv6str
    ipr=re_ip6.search(ipv6str)
    if ipr==None:
        print '无法自动获取ipv6，请确认连接正常或换用合适的获取ip地址，或手工输入ip'
        sys.exit()
    else:

        ip6=ipr.group()
print 'ip6:',ip6



httpsHandler = urllib2.HTTPSHandler()
opener = urllib2.build_opener(httpsHandler)
urllib2.install_opener(opener)
url_s='https://dnsapi.cn/Domain.List'
query_args = dict(pub_postdata)
query_args.update({'type':'mine'})
request = urllib2.Request(url_s)
request.add_data(urllib.urlencode(query_args))
request.add_header('User-agent',user_agent_str)
json_str=urllib2.urlopen(request ).read()
#r=urllib2.urlopen('https://dnsapi.cn/Domain.Id',encoded_args).read()
#print r

#print json_str

#print 'decoding'
data=json.loads(json_str)
#print data
domain_id=0
for domain_d in data['domains']:
    if domain_d['name'] == user_domain:
        domain_id=domain_d['id']
        #print domain_id

for ri in user_subdomain:
    url_s='https://dnsapi.cn/Record.List'
    query_args = dict(pub_postdata)
    query_args.update({'domain_id':domain_id,'sub_domain':ri})
    request = urllib2.Request(url_s)
    request.add_data(urllib.urlencode(query_args))
    request.add_header('User-agent', user_agent_str)
    json_str=urllib2.urlopen(request).read()
    #print json_str
    #print 'decoding'
    data=json.loads(json_str)
    url_s='https://dnsapi.cn/Record.Modify'
    for rdata in data['records']:

        rid=rdata['id']
        rtype=rdata['type']
        if rtype== "A":
            query_args = dict(pub_postdata)
            q1 = {'record_id':rid,'domain_id':domain_id,'sub_domain':ri,\
                  'ttl':ttl,'record_type':'A',\
                   'record_line':'默认','value':ip}
            query_args.update(q1)
            request = urllib2.Request(url_s)
            request.add_data(urllib.urlencode(query_args))
            request.add_header('User-agent', user_agent_str)
            json_str=urllib2.urlopen(request).read()
            print json_str
            ldata=json.loads(json_str)
            if ldata["status"]["code"] !='1':
                print ldata["status"]["code"],"errors happened ==========="
                print ldata

        if len(ip6)>3 and rtype=="AAAA":
            query_args = dict(pub_postdata)
            q1 = {'record_id':rid,'domain_id':domain_id,'sub_domain':ri,\
                  'ttl':ttl,'record_type':'AAAA',\
                   'record_line':'默认','value':ip6}
            query_args.update(q1)
            request = urllib2.Request(url_s)
            request.add_data(urllib.urlencode(query_args))
            request.add_header('User-agent', user_agent_str)
            json_str=urllib2.urlopen(request).read()
            print json_str
            ldata=json.loads(json_str)
            if ldata["status"]["code"] !='1':
                print ldata["status"]["code"],"errors happened ==========="
                print ldata

