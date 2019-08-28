"""
file: GPSDevice.py
Implement later
@author: Will Merges
"""

class GPS_Device(object):

    def __init__(self, logger):
        self.logger = logger

        self.lat = None
        self.long = None
        self.alt = None
        self.time = None

        self.update = False

    def refresh(self):
        #parse data string if available (implemented by children)
        #let the logger know
        if logger not None:
            logger.GPS_update()

    def get_logger(self):
        return self.logger

#example
class AdafruitUltimateGPS(GPS_Device):
    def __init__(self):
