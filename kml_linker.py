import simplekml

# globals
KML_SAVE_NAME = "main.kml"
kml = None

"""
add a network link to a kml file
link_file is somefile.kml to link to
"""
def add_netlink(kml: simplekml.Kml, link_file: str):
    netlink = kml.newnetworklink(name=link_file)
    netlink.link.href = link_file
    netlink.link.viewrefreshmode = simplekml.ViewRefreshMode.onrequest
    write_main()

"""
create main document
"""
def create_main():
    kml = simplekml.Kml()
    write_main()

"""
write out main document
"""
def write_main():
    if kml is not None:
        kml.save(KML_SAVE_NAME)
