from Upgrade import *
import time

# e.g data_file = 'C:/User/compname/Desktop/readme.txt'
data_file = 'C:/Users/jmendez/Documents/Napalm/table.txt'
mac_list = list()                               # used to identify bind devices
file = ''

""" Opens file and grabs mac and appends to mac_list"""
temp_file = open(data_file, 'r')                # Opens file as read only
for sentence in temp_file:                      # Grabs pre-existing data
    temp_mac, __, __ = sentence.split()         # Need mac as identifier
    mac_list.append(temp_mac)                   # Means device already bind don't add
temp_file.close()                               # close file

""" Connect to DHCP Server and obtain bindings"""
DHCP_Server = FastIron('10.176.217.148')        # Connects to DHCP Server
DHCP_Server.open()                              # Opens connection
bindings = DHCP_Server.obtain_binding()         # Parses bindings returns dictionary

""" Save binding to a file"""
file = open(data_file, 'a')                     # Opens saving file
for mac_key in bindings:                        # grabs mac
    if mac_key not in mac_list:                 # checks if device not in binding
        mac_list.append(mac_key)                # new device added to binding
        ip = bindings.get(mac_key).get('ip')    # ip add for telnet
        ser = bindings.get(mac_key).get('serial')   # serial for later conversion
        temp_string = mac_key + " " + ip + " " + str(ser) + '\n'    # string to save
        file.write(temp_string)                 # saved to file as single string
file.close()                                    # closed file
DHCP_Server.close()                             # DHCP server connection closed


"""Connect to devices using IP bindings obtained"""

"""Push default security configuration"""

"""Grab Actual security configuration"""

"""Map serial # to configuration and push respective config"""


