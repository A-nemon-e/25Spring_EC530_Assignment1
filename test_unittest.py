import pytest
from unittest.mock import patch
from geopy.distance import GeodesicDistance
from main import (
    calculate_distance,
    find_closest_point,
    match_points,
    is_valid_latitude,
    is_valid_longitude,
    get_coordinates_from_input
)  

# 测试数据
valid_coordinate1 = (40.7128, -74.0060)  # 纽约
valid_coordinate2 = (34.0522, -118.2437)  # 洛杉矶
valid_coordinate3 = (41.8781, -87.6298) # 芝加哥
# from main import (  
#     calculate_distance,
#     find_closest_point,
#     match_points,
#     is_valid_latitude,
#     is_valid_longitude,
#     get_coordinates_from_input
# )
from main import *


valid_coordinate1 = (40.7128, -74.0060)  
valid_coordinate2 = (34.0522, -118.2437) 
valid_coordinate3 = (41.8781, -87.6298)

invalid_latitude = (91.0, 0.0)
invalid_longitude = (0.0, 181.0)

edge_case_latitude = (-90.0, -74.0)
edge_case_longitude = (34.0522, 180.0)
empty_array = []
array1 = [valid_coordinate1, valid_coordinate2]
array2 = [valid_coordinate2, valid_coordinate3]


# calculate_distance
def test_calculate_distance_valid():
    expected_distance = GeodesicDistance(valid_coordinate1, valid_coordinate2).km
    assert calculate_distance(valid_coordinate1, valid_coordinate2) == pytest.approx(expected_distance)

def test_calculate_distance_same_point():
    assert calculate_distance(valid_coordinate1, valid_coordinate1) == 0.0


# find_closest_point
def test_find_closest_point_valid():
    assert find_closest_point(valid_coordinate2, array2) == valid_coordinate2

def test_find_closest_point_empty_array():
    assert find_closest_point(valid_coordinate1, empty_array) is None


# match_points
def test_match_points_valid():
    expected_matches = {
        valid_coordinate1: valid_coordinate3,
        valid_coordinate2: valid_coordinate2,
    }
    assert match_points(array1, array2) == expected_matches

def test_match_points_empty_arrays():
    assert match_points(empty_array, empty_array) == {}


# 
def test_is_valid_latitude_valid():
    assert is_valid_latitude(valid_coordinate1[0]) is True

def test_is_valid_latitude_invalid():
    assert is_valid_latitude(invalid_latitude[0]) is False

def test_is_valid_latitude_edge_case():
    assert is_valid_latitude(edge_case_latitude[0]) is True

def test_is_valid_latitude_invalid_type():
    assert is_valid_latitude("abc") is False


# 
def test_is_valid_longitude_valid():
    assert is_valid_longitude(valid_coordinate1[1]) is True

def test_is_valid_longitude_invalid():
    assert is_valid_longitude(invalid_longitude[1]) is False

def test_is_valid_longitude_edge_case():
    assert is_valid_longitude(edge_case_longitude[1]) is True

def test_is_valid_longitude_invalid_type():
    assert is_valid_longitude("xyz") is False

# Test cases
def test_get_coordinates_from_input_valid(monkeypatch):
    # Test case 1: Valid input
    user_input = "[(40.7128, -74.0060), (34.0522, -118.2437)]"
    monkeypatch.setattr('builtins.input', lambda: user_input)
    result = get_coordinates_from_input("test_array")
    assert result == [(40.7128, -74.0060), (34.0522, -118.2437)]

    # Test case 2: Valid input with extra whitespace
    user_input = "  [ ( 40.7128 , -74.0060 ) , (34.0522,-118.2437) ]  "
    monkeypatch.setattr('builtins.input', lambda: user_input)
    result = get_coordinates_from_input("test_array")
    assert result == [(40.7128, -74.0060), (34.0522, -118.2437)]


def test_get_coordinates_from_input_invalid_format(monkeypatch):
    user_input=[]
    # Test case 1: Invalid format - missing brackets
    user_input.append("(40.7128, -74.0060), (34.0522, -118.2437)")
    # monkeypatch.setattr('builtins.input', lambda: user_input)
    # with pytest.raises(ValueError, match="Invalid input format."):
    #     get_coordinates_from_input("test_array")

    # Test case 2: Invalid format - incorrect brackets
    user_input.append("{40.7128, -74.0060}, {34.0522, -118.2437}")
    # monkeypatch.setattr('builtins.input', lambda: user_input)
    # with pytest.raises(ValueError, match="Invalid input format."):
    #     get_coordinates_from_input("test_array")

     # Test case 3: Invalid format - missing comma between tuples
    user_input.append("[(40.7128, -74.0060) (34.0522, -118.2437)]")  # Missing comma

    monkeypatch.setattr('builtins.input', lambda: user_input.pop(0))
    with pytest.raises(Exception):
        get_coordinates_from_input("test_array")



def test_get_coordinates_from_input_invalid_values(monkeypatch):
    # Test case 1: Invalid latitude
    user_input=[]
    user_input.append("[(100, -74.0060)]")
    # monkeypatch.setattr('builtins.input', lambda: user_input)
    # with pytest.raises(ValueError, match="Invalid input format."):  # Or check print output
    #     get_coordinates_from_input("test_array")

    # Test case 2: Invalid longitude
    user_input.append("[(40.7128, -200)]")
    # monkeypatch.setattr('builtins.input', lambda: user_input)
    # with pytest.raises(ValueError, match="Invalid input format."): # Or check print output
    #     get_coordinates_from_input("test_array")

    # Test case 3: One valid, one invalid coordinate
    user_input.append("[(40.7128, -74.0060), (100, -118.2437)]")
    monkeypatch.setattr('builtins.input', lambda: user_input.pop(0))
    with pytest.raises(Exception): # Or check print output
        get_coordinates_from_input("test_array")


def test_get_coordinates_from_input_empty(monkeypatch):
    user_input = "[]"
    monkeypatch.setattr('builtins.input', lambda: user_input)
    result = get_coordinates_from_input("test_array")
    assert result == []





# Decorators below is generated by Google Gemini.
# This is to immitate user input to the stdin.

@patch('builtins.input', return_value='[(40.7128, -74.0060), (34.0522, -118.2437)]')
def test_get_coordinates_from_input_valid(mock_input):
    result = get_coordinates_from_input("array1")
    assert result == [(40.7128, -74.0060), (34.0522, -118.2437)]

@patch('builtins.input', side_effect=['invalid input', '[(91.0, 0.0)]', '[(40.7128, -74.0060), (34.0522, -118.2437)]'])
def test_get_coordinates_from_input_invalid(mock_input):
    result = get_coordinates_from_input("array1")
    assert result == [(40.7128, -74.0060), (34.0522, -118.2437)]