from math import radians, sin, cos, sqrt, atan2


def geofencing(latitude, longitude):
    latitude = latitude
    longitude = longitude

    if latitude is None or longitude is None:
        return False

    geo_lat = 19.1950125
    geo_lon = 72.9544889
    lat = float(latitude)
    lon = float(longitude)

    # In Meters
    radius_of_distance = 65

    geo_lat, geo_lon, lat, lon = map(radians, [geo_lat, geo_lon, lat, lon])

    dlon = lon - geo_lon
    dlat = lat - geo_lat
    a = sin(dlat / 2) ** 2 + cos(geo_lat) * cos(geo_lon) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c * 1000

    if distance <= radius_of_distance:
        return True
    else:
        return False
