from math import radians, cos, sin, asin, sqrt


def Solve_Haversine(lon1: float, lat1: float, lon2: float, lat2: float, distancetype) -> float:
    """

    All arguments must be of equal length.
    :param lon1: longitude of first place
    :param lat1: latitude of first place
    :param lon2: longitude of second place
    :param lat2: latitude of second place
    :return: distance in meters between the two sets of coordinates
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers

    if distancetype == "meters":
        return c * r
    elif distancetype == "kilometers":
        return c * r * 0.001
    elif distancetype == "miles":
        return c * r * 0.000621371
    elif distancetype == "centimeters":
        return c * r * 100
    elif distancetype == "inches":
        return c * r * 39.3701