"""
file: GPSDevice.py
Implement later
@author: Will Merges
"""
import _thread
import sys

class GPSDevice(object):

    def __init__(self):
        self.lat = None
        self.long = None
        self.alt = None
        self.time = None

        self.update = False

        self.exit = False
        try:
            self.thread = _thread.start_new_thread(self.run, ())
        except:
            print("failed to start thread", file=sys.stderr)

    def run(self):
        while not self.exit:
            self.update_loop()

    def kill(self):
        self.exit = True

    #should ovverride in implementations
    def refresh(self):
        #parse data string if available (implemented by children)
        pass

    def update_loop(self):
        self.refresh()
        self.update = True

#example
class AdafruitUltimateGPS(GPS_Device):
    def __init__(self):
        super().__init__()

    def refresh(self):
        #do stuff
        pass
