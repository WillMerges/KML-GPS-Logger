import simplekml

# globals
KML_SAVE_NAME = "main.kml"
kml = None

"""
add a network link to a kml file
"""
def add_netlink(kml: simplekml.Kml, link_file: str):
    netlink = kml.newnetworklink(name=link_file)
    netlink.link.href = name_str+".kml"
    netlink.link.viewrefreshmode = simplekml.ViewRefreshMode.onrequest

"""
create main document
"""
def create_main():
    kml = simplekml.Kml()

"""
write out main document
"""
def write_main():
    if kml is not None:
        kml.save(KML_SAVE_NAME)
