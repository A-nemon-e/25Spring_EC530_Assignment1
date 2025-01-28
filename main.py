from geopy.distance import geodesic


def match_points(array1, array2):
  """
array: lat, lon
  """
  matches = {}
  for point1 in array1:
    min_distance = float('inf') 
    for i, point2 in enumerate(array2):
      curr_distance = geodesic(point1, point2).km
      if curr_distance < min_distance:
        min_distance = curr_distance
        matches[point1] = point2
  return matches


def get_coordinates_from_input(array_name):
    # This function is written by Google Gemini
    while True:
        print(f"Enter coordinates for {array_name} in the format [(lat1, lon1), (lat2, lon2), ...].")
        input_str = input("> ")
        try:
            coordinates = eval(input_str) 
            if isinstance(coordinates, list) and all(isinstance(coord, tuple) and len(coord) == 2 for coord in coordinates):
                
                return coordinates
            else:
                print("Invalid input format. Please enter a list of (lat, lon) pairs.")
        except (ValueError, SyntaxError, NameError):
            print("Invalid input. Please enter a valid Python list of tuples.")


# array1 = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298), (31.25649, 120.126668)] 
# array2 = [(37.7749, -122.4194), (40.6500, -73.9499), (34.0585,-118.2426), (41.8818, -87.6278)]  
array1 = get_coordinates_from_input("array1")
array2 = get_coordinates_from_input("array2")

matches = match_points(array1, array2)
print(f"Results: {matches}") 
