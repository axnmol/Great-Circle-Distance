# Great-Circle-Distance
This is a python program capable of calculating great-circle distance between two coordinates, using haversine formula.
The great-circle distance, orthodromic distance, or spherical distance is the shortest distance between two points on the surface of a sphere, measured along the surface of the sphere (as opposed to a straight line through the sphere's interior).

More emphasis is paid on the efficiency of the calculation hence haversine formula is being used which considers Earth as a perfect square. It turns out to be having only error of 0.5%. If accuracy and precision would have been our goal than using Vincenty's formulae would turn out to be a better choice. As it doesn't consider Earth as a sphere rather an ellipsoid.

Example implementation reads from a file with lines having data with the following format: {"id":"1", latitude": "52.986375", "longitude": "-6.043701"} and finds ids within the given perimeter. The locations.json file contains the coordinates of various location with their respective location ids.

Further given a list of directed paths connecting specific GPS locations on earth, Dijkstra's algorithm (As the distances are always non-negative) is used to give shortest distance between two locations and the followed path.

The paths.json file contains the connected paths in json format having data as: { "start": 24, "end": 21 }, giving the location ids of the starting and ending node.
Further each files contains vital comments regarding the implementaion.
