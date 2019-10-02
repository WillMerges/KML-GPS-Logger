"""
file: GPSTrack.py
makes a kml document containing a gxtrack that is update by a GPSDevice.GPSDevice object
@author: Will Merges
"""
import simplekml
from GPSDevice import GPSDevice

class GPSTrack(object):

    """
    name is name of doc without .kml extension
    """
    def __init__(self, gps: GPSDevice, name: str):
        self.name = name
        self.times = []
        self.coords = []
        self.size = 0 #number of points collected
        self.gps = gps

        self.kml = simplekml.Kml(name=self.name+".kml", open=1)
        self.track = self.kml.newgxtrack(name = self.name)

        self.track.stylemap.normalstyle.iconstyle.icon.href = 'resources/track-0.png'
        self.track.stylemap.normalstyle.linestyle.color = '99ffac59'
        self.track.stylemap.normalstyle.linestyle.width = 6
        self.track.stylemap.highlightstyle.iconstyle.icon.href = 'resources/track-0.png'
        self.track.stylemap.highlightstyle.iconstyle.scale = 1.2
        self.track.stylemap.highlightstyle.linestyle.color = '99ffac59'
        self.track.stylemap.highlightstyle.linestyle.width = 8

    def update_track(self):
        if self.gps.update:
            self.size = self.size + 1
            self.times.append(self.gps.time)
            self.coords.append((self.gps.lat, self.gps.long, self.gps.alt))
            self.gps.update = False
            self.write_track()
        #change the self.kml.lookat data to lookat most recent data entries

    def write_track(self):
        self.track.newwhen(self.times)
        self.track.newgxcoord(self.coords)
        self.kml.save(self.name + ".kml")

#how to use
"""
dev = GPSDevice()
gps = GPSTrack(dev, "test")
while 1:
    gps.update_track()
"""
