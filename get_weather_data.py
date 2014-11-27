
# ===================================================================
# ||            Hourly Weather Getter v.1 - 11/18/2014             ||
# ||                      Jeremy Pernicek                          ||
# ||                                                               ||
# || This script downloads .csv files from wunderground.com that   ||
# || have hourly weather data for Pittsburgh, PA. Data includes    ||
# || Times, Temp, Dew Point, Humidity, Wind, Conditions, DateUTC,  ||
# || & several other variables.                                    ||                            
# || required: urlib      										   ||
# || Make sure to change the directory variable                    ||
# ===================================================================

# Headers:
# TimeEST,TemperatureF,Dew PointF,Humidity,Sea Level PressureIn,VisibilityMPH,
# Wind Direction,Wind SpeedMPH,Gust SpeedMPH,PrecipitationIn,Events,Conditions,
# WindDirDegrees,DateUTC<br />

# e.g. of an observation:
# 12:51 AM,50.0,43.0,77,30.03,10.0,SSE,4.6,-,N/A,,Overcast,160,2011-01-01 05:51:00

import urllib

# wunderground provides a link to capture hourly data in .csv format
# the link is programmable, you can just continually add to the # of days to get the following day
startLink = "http://www.wunderground.com/history/airport/KPIT/2014/07/"
endLink = "/DailyHistory.html?format=1"

# 10/7-10/26 = 
# 10/27-11/9
# 11/10-11/16

# (365*3)+1+279 = 1375 days : +1 day for leap year in 2012 and 279 days in 2014
# .\data try this instead of the full path
# Loop to retrieve 1375 days worth of hourly .csv files
for day in xrange(1, 20):
        #build link by inserting loop variable into link
		url = startLink+str(day)+endLink
		#retrieve .csv file from url
		response = urllib.urlopen(url)
		#create unique file name
		dir = "C:\Users\JP\Desktop\validation\data\\"
		fileName = dir+"day"+str(day)+".csv"
		#write to .csv file
		localFile = open(fileName, 'w')
		localFile.write(response.read())
		localFile.close()

		