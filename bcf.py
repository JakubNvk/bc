import imhdsk
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


def getCoordinates(address):
    ''' Returns coordinates for given address. '''
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    return [location.latitude, location.longitude]

def getDistance(point_a, point_b):
    ''' Returns distance in meters and seconds between given points. '''
    distance_meters = int(vincenty(point_a, point_b).meters)
    distance_seconds = int(distance_meters)/1.4
    # 1.4m/s is the average walking speed of a human
    return [distance_meters, distance_seconds]

def getFirstRoute(frm, to):
    ''' Returns first available route. '''
    routes = imhdsk.routes(frm, to, time='', date='')
    if len(routes) > 0:
        return routes[0]
    print 'No route found!'

def getRoutes(frm, to):
    ''' Returns all available routes. '''
    routes = imhdsk.routes(frm, to, time='', date='')
    if len(routes) > 0:
        return routes
    print 'No routes found!'

def getStopLocation(name):
    ''' Returns latitude and longitude of bus stop called <name>. '''
    stops = open('stops/stops.txt', 'r')
    for line in stops:
        if line == name:
            return next(stops)

def getNearestStop(location):
    ''' Returns nearest stop to the provided location. '''

"""
class Spoj(imhdsk.Drive):

    FORMAT = 'Line {0} leaving {1} from {2} arriving {3} at {4}.'

    def __init(self, Drive):
        self.Drive = Drive

    def __repr__(self):
        return self.Drive.start + self.Drive.dest
"""