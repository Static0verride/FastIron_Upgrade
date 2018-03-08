from Upgrade import *
import time


""" Connect to DHCP Server and obtain bindings"""
DHCP_Server = FastIron('10.176.217.148')
DHCP_Server.open()
print(DHCP_Server.obtain_binding())
DHCP_Server.close()
"""Connect to devices using IP bindings obtained"""

"""Push default security configuration"""

"""Grab Actual security configuration"""

"""Map serial # to configuration and push respective config"""


