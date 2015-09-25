import sys
import json
import csv
import urllib2

# assignment 1
## python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx B52
## api key: f97a9bac-7b8f-431f-acb3-f6f9d44716b6

__author__='Siying Zhang'


if __name__=='__main__':
	# Retrieve key and bus number from command line
	key = sys.argv[1]
	busLine = sys.argv[2]

	# Request for json file from url given
	url = urllib2.Request('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key, busLine))
	request = urllib2.urlopen(url)
	busData = json.load(request)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	
	# Output
	print "Bus Line:", busLine
	print "Number of Active Buses: %d" %len(busData)
	for i in range(0,len(busData)):
		vehicleLoc = busData[i]['MonitoredVehicleJourney']['VehicleLocation']
		print "Bus %d is at latitude %f and longitude %f" % (i, vehicleLoc['Latitude'],vehicleLoc['Longitude'])