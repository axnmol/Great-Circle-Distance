import math

EARTH_RADIUS = 6371.009  # km


class Location:

    def __init__(self, lat, lon):
        if lat < -90.0 or lat > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0")

        if lon < -180.0 or lon > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0")

        self.lat = float(lat)
        self.lon = float(lon)

# method to retrieve coordinated from records
    @classmethod
    def from_record(cls, data):
        try:
            obj = cls(float(data["latitude"]), float(data["longitude"]))
        except KeyError:
            raise ValueError("Required fields: latitude, longitude")
        return obj

# locationrad class supervising coordinates to radians conversion
    class Locationrad:
        def __init__(self, lat, lon):
            self.lat = lat
            self.lon = lon

        @classmethod
        def from_decimal(cls, lat, lon):
            return cls(math.radians(lat), math.radians(lon))

        def __sub__(self, other):
            if isinstance(other, Location.Locationrad):
                return Location.Locationrad(self.lat - other.lat, self.lon - other.lon)
            else:
                raise NotImplementedError

    @property
    def radians(self):
        return Location.Locationrad.from_decimal(self.lat, self.lon)

# getting distance by applying haversine formula
    def dist_to(self, other, radius=EARTH_RADIUS):
        diff = self.radians - other.radians
        A = math.sin(abs(diff.lat) / 2) ** 2
        B = math.cos(self.radians.lat) * math.cos(other.radians.lat) * \
            math.sin(abs(diff.lon) / 2) ** 2
        haversine = 2 * math.asin(math.sqrt(A + B))
        return radius * haversine

# function telling if location is inside the perimeter radius or not
    def within_dist(self, other: "Location", max_dist: float):
        return self.dist_to(other) <= max_dist
