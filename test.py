import logging
import requests
import json

log_name = 'python_req_log.txt'
logging.basicConfig(filename=log_name,format='%(asctime)s %(levelname)s: %(message)s',datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.DEBUG)

logging.info("Begin")
logging.info("Asking user for device type")
# Ask the user what kind of list they want to create
device_type = input("Do you want to create a list of [r]outers or [s]witches?")

# create a variable called type to hold which kind of device to save
if device_type == 'r':
        type = "ROUTER"
else:
        type = "SWITCH"

logging.info("Device type is " + type)

# Ask user for name of the file
file_name = input("Specify the file name to use for the list:")

logging.info("Will save device list to " + file_name)

# Get Count of Devices
# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "https://sandboxapic.cisco.com"

# Specify URL for the devices count
devices_count_url = controller_url + '/api/v0/network-device/count'

logging.info("Calling APIC-EM API url:" + devices_count_url)

# Perform GET on devices_count_url
devices_count_response = requests.get(devices_count_url, verify=False)
count = devices_count_response.json()["response"]

logging.debug("API response: " + json.dumps(devices_count_response.json(), indent=4, separators=(',', ': ')))

# Get Devices
# This function allows you to view a list of all the devices in the network.
# We will specify that the list should start with the first device (1) and end with the last device which is the count of all the devices
# we retrieved in the previous step
get_devices_url = controller_url + '/api/v0/network-device/1/' + str(count)

logging.info("Calling APIC-EM API url:" + get_devices_url)
#Perform GET on get_devices_url
get_devices_response = requests.get(get_devices_url, verify=False)

# The json method of the response object returned by requests.get returns the request body in json format
get_devices_json = get_devices_response.json()

logging.debug("API response: " + json.dumps(get_devices_response.json(), indent=4, separators=(',', ': ')))

#Now let's parse the json and write the devices out to our file
# set our parent as the top level response object
parent =  get_devices_json["response"]

# you can open the file using 'with'.
# 'with' gives you better exception handling and when you use 'with' the file automatically be closed
with open(file_name, "w") as file:
    logging.info("File opened:" + file_name)
    logging.info("Begin writing list:" + file_name)
    file.write ("The list of devices of type: " + type + "\n" )
    # for each device returned, write the networkDeviceId and type value to the file
    for item in parent:
         if item["type"] == type:
             file.write ("switch type = " + item["family"] + " id = " + item["id"] + " type = " + item["type"] + "\n")

    logging.info("End writing list:" + file_name)

logging.info("End Program")