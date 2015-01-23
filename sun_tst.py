#!/usr/bin/python
import datetime
from sunrise import sun

s = sun(lat=53.664,long=-2.671)

sunup = s.sunrise(when=datetime.datetime.now())
sundown = s.sunset(when=datetime.datetime.now())

tmp=datetime.datetime.now()
# print tmp.hour
# print tmp.minute
# print tmp.second

now = datetime.time(tmp.hour,tmp.minute,tmp.second)
print now

if now > sunup and now < sundown:
    print "Day"
else:
    print "Night"
print('sunrise at ',s.sunrise(when=datetime.datetime.now()))
print('sunset  at ',s.sunset(when=datetime.datetime.now()))
