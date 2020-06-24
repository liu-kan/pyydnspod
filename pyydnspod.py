#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import urllib.request, urllib.error, urllib.parse
import json,base64
import sys,re
tid='Your token ID' # or username
token='Your Token'
user_domain ='Your domain' # eg. websitename.com
user_subdomain=['@','www'] # input your subdomain as list
name_server='name.com' # name.com or dnspod.cn

ip_add='http://ip-show.com'
ip_add6='http://whatismyv6.com'

#user_subdomain为要设置的子域名，如www
ttl='600' #免费用户最低600
#ip_add='http://api.hostip.info/get_html.php'
#ip_add为获取ip的网址，该网址应该以最尽可能简洁的模式显示ip地址，
#不能连接国外网络的可以使用'http://www.zzsky.cn/code/ip/ip12.asp'
#也可以直接填入ip
#设置结束

login_token=tid+','+token
pub_postdata={'login_token':login_token,'format':'json','lang':'en'}
user_agent_str='PyDdnsClient/1.1.1 (liukan@126.com)'
p_ip=re.compile(r'^http.*')
ip=''
if p_ip.search(ip_add)==None:
    ip=ip_add
else:
    f = urllib.request.urlopen(ip_add)
    re_ip=re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
    ipr=re_ip.search(f.read().decode('utf-8'))
    if ipr==None:
        print('无法自动获取ip，请确认连接正常或换用合适的获取ip地址，或手工输入ip')
        sys.exit()
    else:
        ip=ipr.group()
print('ip:',ip)

p_ip=re.compile(r'^http.*')
ip6=''
if p_ip.search(ip_add6)==None:
    ip6=ip_add6
else:
    f = urllib.request.urlopen(ip_add6)
    re_ip6=re.compile('(?:(?:[0-9A-Fa-f]{1,4}:){6}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::(?:[0-9A-Fa-f]{1,4}:){5}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){4}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){3}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,2}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:){2}(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,4}[0-9A-Fa-f]{1,4})?::(?:[0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(?:(?:[0-9A-Fa-f]{1,4}:){,5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(?:(?:[0-9A-Fa-f]{1,4}:){,6}[0-9A-Fa-f]{1,4})?::)(?:%25(?:[A-Za-z0-9\\-._~]|%[0-9A-Fa-f]{2})+)?')
    ipv6str=f.read()
    #print ipv6str
    ipr=re_ip6.search(ipv6str.decode('utf-8'))
    if ipr==None:
        print('无法自动获取ipv6，请确认连接正常或换用合适的获取ip地址，或手工输入ip')
    else:
        ip6=ipr.group()
print('ip6:',ip6)

httpsHandler = urllib.request.HTTPSHandler()
opener = urllib.request.build_opener(httpsHandler)
urllib.request.install_opener(opener)
if name_server=='name.com':
    class PutRequest(urllib.request.Request):
        '''class to handling putting with urllib2'''
        def get_method(self, *args, **kwargs):
            return 'PUT'
    url_s='https://api.name.com/v4/domains/'+user_domain+'/records'
    #base64string = base64.encodestring('%s:%s' % (tid, token)).replace('\n', '')
    base64string = base64.b64encode(bytes('%s:%s' % (tid, token),"utf-8")).decode("utf-8").replace('\n', '')
    request = urllib.request.Request(url_s)
    request.add_header("Authorization", "Basic %s" % base64string)  
    request.add_header('User-agent',user_agent_str)
    json_str=urllib.request.urlopen(request ).read()
    records=json.loads(json_str)
    # print(records)
    if len(ip)>3:
        for subdomain in user_subdomain:
            for record in records['records']:
                # print(record)
                if 'host' in record:
                    if record['host']==subdomain and record['type']=='A':
                        record_id=record['id']
                        url_s='https://api.name.com/v4/domains/'+user_domain+'/records/'+str(record_id)
                        base64string = base64.b64encode(bytes('%s:%s' % (tid, token),"utf-8")).decode("utf-8").replace('\n', '')
                        request = PutRequest(url_s)
                        request.add_header("Authorization", "Basic %s" % base64string)  
                        request.add_header('User-agent',user_agent_str)
                        request.add_header('Content-Type', "application/json")
                        #{"host":"home","type":"A","answer":"10.0.0.1","ttl":300}
                        jdict=dict({"host":subdomain,"type":"A","answer":ip,"ttl":ttl})
                        request.data=json.dumps(jdict).encode("utf-8")
                        json_str=urllib.request.urlopen(request ).read()
                        print(json_str)
    if len(ip6)>3:
        for subdomain in user_subdomain:
            for record in records['records']:
                # print(record)
                if 'host' in record:
                    if record['host']==subdomain and record['type']=='AAAA':
                        record_id=record['id']
                        url_s='https://api.name.com/v4/domains/'+user_domain+'/records/'+str(record_id)
                        base64string = base64.b64encode(bytes('%s:%s' % (tid, token),"utf-8")).decode("utf-8").replace('\n', '')
                        request = PutRequest(url_s)
                        request.add_header("Authorization", "Basic %s" % base64string)  
                        request.add_header('User-agent',user_agent_str)
                        request.add_header('Content-Type', "application/json")                    
                        jdict=dict({"host":subdomain,"type":"AAAA","answer":ip6,"ttl":ttl})
                        request.data=json.dumps(jdict).encode("utf-8")
                        json_str=urllib.request.urlopen(request ).read()
                        print(json_str)

if name_server=='dnspod.cn':
    url_s='https://dnsapi.cn/Domain.List'
    query_args = dict(pub_postdata)
    query_args.update({'type':'mine'})
    request = urllib.request.Request(url_s)
    request.add_data(urllib.parse.urlencode(query_args))
    request.add_header('User-agent',user_agent_str)
    json_str=urllib.request.urlopen(request ).read()
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
        request = urllib.request.Request(url_s)
        request.add_data(urllib.parse.urlencode(query_args))
        request.add_header('User-agent', user_agent_str)
        json_str=urllib.request.urlopen(request).read()
        #print json_str
        #print 'decoding'
        data=json.loads(json_str)
        url_s='https://dnsapi.cn/Record.Modify'
        for rdata in data['records']:

            rid=rdata['id']
            rtype=rdata['type']
            if len(ip)>3 and rtype== "A":
                query_args = dict(pub_postdata)
                q1 = {'record_id':rid,'domain_id':domain_id,'sub_domain':ri,\
                    'ttl':ttl,'record_type':'A',\
                    'record_line':'默认','value':ip}
                query_args.update(q1)
                request = urllib.request.Request(url_s)
                request.add_data(urllib.parse.urlencode(query_args))
                request.add_header('User-agent', user_agent_str)
                json_str=urllib.request.urlopen(request).read()
                print(json_str)
                ldata=json.loads(json_str)
                if ldata["status"]["code"] !='1':
                    print(ldata["status"]["code"],"errors happened ===========")
                    print(ldata)

            if len(ip6)>3 and rtype=="AAAA":
                query_args = dict(pub_postdata)
                q1 = {'record_id':rid,'domain_id':domain_id,'sub_domain':ri,\
                    'ttl':ttl,'record_type':'AAAA',\
                    'record_line':'默认','value':ip6}
                query_args.update(q1)
                request = urllib.request.Request(url_s)
                request.add_data(urllib.parse.urlencode(query_args))
                request.add_header('User-agent', user_agent_str)
                json_str=urllib.request.urlopen(request).read()
                print(json_str)
                ldata=json.loads(json_str)
                if ldata["status"]["code"] !='1':
                    print(ldata["status"]["code"],"errors happened ===========")
                    print(ldata)

