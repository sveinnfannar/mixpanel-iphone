import urllib2
import plistlib
import sys

carriers =  urllib2.urlopen("http://numberportabilitylookup.com/img/networks.csv").readlines()
carriers = map(lambda x : x.split(","), carriers)
carriers = map(lambda x : map(lambda y : y.strip("\n \""), x), carriers)
carriers = filter(lambda x : len(x) == 3, carriers)
carriers = map(lambda x : (x[1], x[2]), carriers)


plistlib.writePlist(dict(carriers), sys.stdout)