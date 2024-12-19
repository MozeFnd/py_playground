from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # radius of the Earth in kilometers
    R = 6371.0

    # convert coordinates to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # differences in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # calculate distance
    distance = R * c

    return distance

# test the function
lat1 = 0
lon1 = 0
lat2 = 30.65
lon2 = 104.07

print(calculate_distance(lat1, lon1, lat2, lon2), "kilometers")