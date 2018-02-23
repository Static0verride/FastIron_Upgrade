from Upgrade import *
import time

Driver = FastIron('10.176.217.151')

Driver.open()
print(Driver.show_version())
Driver.close()

