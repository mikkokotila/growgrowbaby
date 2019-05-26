import grovepi
import os
import math
import time
import SI1145

from ISStreamer.Streamer import Streamer
streamer = Streamer(bucket_name='Grow', 
                    bucket_key='dht', 
                    access_key='ist_NH72MhfG17ntot3lP1wPkqSZE4YyR9Mc')

# config
humidity_ceiling = 98

def get_timestamp():
    return time.strftime('%D/%T')

def write_log(to_write):
    f = open('/tmp/sensors.log', 'a')
    f.write(to_write + '\n')
    f.close()

# GrovePi+ port numbers
hcho_sensor = 0
temperature_sensor = 4
water_sensor = 3

light_sensor = SI1145.SI1145()

while True:
    try:
        start = time.time()
        # get the timestamp for obervation
        timestamp = get_timestamp()

    	# get temperature and humidity readings
        [temp, humidity] = grovepi.dht(temperature_sensor, 1)
		
        # get hcho gas reading and voltage
	hcho = grovepi.analogRead(hcho_sensor)
	voltage = float(hcho * 5 / 1024)

	# water status
	water_status = grovepi.pinMode(water_sensor, "INPUT")

	# light related 
	visibility =  light_sensor.readVisible()
        ir = light_sensor.readIR()
        uv = light_sensor.readUV()

	# parse the results together
	data = [timestamp, temp, humidity, hcho, voltage,
                water_status, visibility, ir, uv]

        # decide if humidity needs to increase
        grovepi.pinMode(2, "OUTPUT")
        if humidity >= humidity_ceiling:
            grovepi.digitalWrite(2, 0)
        else:
            grovepi.digitalWrite(2, 1)

        # send to streaming analytics service
        streamer.log("Temp", temp)
        streamer.log("Humidity", humidity)
        streamer.log("HCHO", hcho)
        streamer.log("Voltage", voltage)
        streamer.log("WaterStatus", water_status)
        streamer.log("Visibility", visibility)
        streamer.log("InfraRed", ir)
        streamer.log("UV", uv)
        streamer.flush()

        to_write = ','.join(str(i) for i in data)

	write_log(to_write)
        end = time.time()

        # wait for a total of 10 seconds
        time.sleep(10 - (end - start))

    except KeyboardInterrupt:
        break

    except IOError:
        print ("Error")
