#!/usr/bin/python
import datetime
from sunrise import sun

def daytime(s):
    sunup = s.sunrise(when=datetime.datetime.now())
    sundown = s.sunset(when=datetime.datetime.now())
    tmp=datetime.datetime.now()
# print tmp.hour
# print tmp.minute
# print tmp.second
    now = datetime.time(tmp.hour,tmp.minute,tmp.second)
    return (now > sunup and now < sundown)


def nightime(s):
    sunup = s.sunrise(when=datetime.datetime.now())
    sundown = s.sunset(when=datetime.datetime.now())
    tmp=datetime.datetime.now()
# print tmp.hour
# print tmp.minute
# print tmp.second
    now = datetime.time(tmp.hour,tmp.minute,tmp.second)
    return (now < sunup and now > sundown)


s = sun(lat=53.664,long=-2.671)
tmp=datetime.datetime.now()
print tmp.hour,":",tmp.minute,":",tmp.second

print "it is day ?  :",daytime( s )
print "it is night ?:",nightime( s )

