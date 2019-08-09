import sys
import simplekml

class GPS_Logger(object):

    def __init__(self, device, flight_name, outfile=None):
        self.device = device
        self.flight_name = flight_name
        if outfile is None:
            self.log_file = sys.stdout
        else:
            try:
                #append to end of previously existing log file if it exists
                self.log_file = open(outfile+".log", "a")
            except:
                print("failed to open logfile '"+logfile+".log")
                self.log_file = sys.stdout

        self.coordinates = [] #(lat, long, alt)
        self.times = []
        self.num_pts = 0

    #must be type Kml.Document or Kml.Folder
    #return None if no track
    def add_track(self, kml_document):
        if self.num_pts == 0:
            return None

        ret = kml_document.newgxtrack(name=flight_name)

        ret.newwhen(self.times)
        self.newgxcoord(self.coordinates)

        trk.stylemap.normalstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
        trk.stylemap.normalstyle.linestyle.color = '99ffac59'
        trk.stylemap.normalstyle.linestyle.width = 6
        trk.stylemap.highlightstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
        trk.stylemap.highlightstyle.iconstyle.scale = 1.2
        trk.stylemap.highlightstyle.linestyle.color = '99ffac59'
        trk.stylemap.highlightstyle.linestyle.width = 8

        return ret

    def GPS_Update(self):
        self.coordinates.append((device.lat, device.long, device.alt))
        self.times.append(device.time)
        self.num_pts = self.num_pts + 1
