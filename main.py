from geopy.distance import geodesic
import re

# def match_points(array1, array2):
#   """
# array: lat, lon
#   """
#   matches = {}
#   for point1 in array1:
#     min_distance = float('inf') 
#     for i, point2 in enumerate(array2):
#       curr_distance = geodesic(point1, point2).km
#       if curr_distance < min_distance:
#         min_distance = curr_distance
#         matches[point1] = point2
#   return matches

def calculate_distance(point1, point2):
  """
  Calculates distance in kilometers.
  """
  return geodesic(point1, point2).km


def find_closest_point(point, array):
  """
  Finds the closest point to the current point (of array1) in array2.
  """
  min_distance = float('inf')
  closest_point = None
  for p in array:
    distance = calculate_distance(point, p)
    if distance < min_distance:
      min_distance = distance
      closest_point = p
  return closest_point


def match_points(array1, array2):
  """
  Generates dict, where keys are points in array1 and values are the matched points in array2.
  """

  matches = {}
  for point1 in array1:
    matches[point1] = find_closest_point(point1, array2)
  return matches


def is_valid_latitude(lat):
    """Checks if a latitude value is valid (between -90 and +90 degrees)."""
    try:
        lat_float = float(lat)
        return -90 <= lat_float <= 90
    except ValueError:
        return False


def is_valid_longitude(lon):
    """Checks if a longitude value is valid (between -180 and +180 degrees)."""
    try:
        lon_float = float(lon)
        return -180 <= lon_float <= 180
    except ValueError:
        return False


def get_coordinates_from_input(array_name):
    """
    Gets coordinates from user input, validates the format and values. Only accepts decimal degrees (e.g., 40.7128, -74.0060) using ±for N/S, E/W.
    This function is modified by Google Gemini.
    """
    while True:
        print(f"Enter coordinates for {array_name} in the format [(lat1, lon1), (lat2, lon2), ...].")
        print("Latitude and longitude must be in decimal degrees (e.g., 40.7128, -74.0060).")
        input_str = input("> ")
        try:
            # Use regular expression to validate the input format
            pattern = r"^\s*\[(\s*\(\s*-?\d+(?:\.\d+)?\s*,\s*-?\d+(?:\.\d+)?\s*\)\s*,?\s*)*\]\s*$"
            if not re.match(pattern, input_str):
                raise ValueError("Invalid input format.")

            coordinates = eval(input_str)

            if isinstance(coordinates, list) and all(
                isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates
            ):
                # Check if each coordinate is valid
                valid_coordinates = []
                for lat, lon in coordinates:
                    if is_valid_latitude(lat) and is_valid_longitude(lon):
                        valid_coordinates.append((float(lat), float(lon)))
                    else:
                        print(
                            f"Invalid coordinate: ({lat}, {lon}). "
                            "Latitude must be between -90 and +90, longitude between -180 and +180."
                        )
                        break  # Exit the loop if an invalid coordinate is found
                else:
                    # If the loop completed without breaking, all coordinates are valid
                    return valid_coordinates
            else:
                print("Invalid input format. Please enter a list of (lat, lon) pairs.")
        except (ValueError, SyntaxError, NameError) as e:
            print(f"Invalid input: {e}. Please enter a valid Python list of tuples.")

# array1 = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298), (31.25649, 120.126668)] 
# array2 = [(37.7749, -122.4194), (40.6500, -73.9499), (34.0585,-118.2426), (41.8818, -87.6278)]  
array1 = get_coordinates_from_input("array1")
array2 = get_coordinates_from_input("array2")

matches = match_points(array1, array2)
print(f"Results: {matches}") 
