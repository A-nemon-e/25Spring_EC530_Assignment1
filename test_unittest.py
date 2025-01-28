import pytest
from geopy.distance import GeodesicDistance
from main import (
    calculate_distance,
    find_closest_point,
    match_points,
    is_valid_latitude,
    is_valid_longitude,
)  

# 测试数据
valid_coordinate1 = (40.7128, -74.0060)  # 纽约
valid_coordinate2 = (34.0522, -118.2437)  # 洛杉矶
valid_coordinate3 = (41.8781, -87.6298) # 芝加哥
invalid_latitude = (91.0, 0.0)
invalid_longitude = (0.0, 181.0)
edge_case_latitude = (-90.0, -74.0)
edge_case_longitude = (34.0522, 180.0)
empty_array = []
array1 = [valid_coordinate1, valid_coordinate2]
array2 = [valid_coordinate2, valid_coordinate3]

# 测试 calculate_distance 函数
def test_calculate_distance_valid():
    # 使用已知的距离来验证
    expected_distance = GeodesicDistance(valid_coordinate1, valid_coordinate2).km
    assert calculate_distance(valid_coordinate1, valid_coordinate2) == pytest.approx(expected_distance)

def test_calculate_distance_same_point():
    assert calculate_distance(valid_coordinate1, valid_coordinate1) == 0.0

# 测试 find_closest_point 函数
def test_find_closest_point_valid():
    assert find_closest_point(valid_coordinate1, array2) == valid_coordinate2

def test_find_closest_point_empty_array():
    assert find_closest_point(valid_coordinate1, empty_array) is None

# 测试 match_points 函数
def test_match_points_valid():
    expected_matches = {
        valid_coordinate1: valid_coordinate2,
        valid_coordinate2: valid_coordinate2,
    }
    assert match_points(array1, array2) == expected_matches

def test_match_points_empty_arrays():
    assert match_points(empty_array, empty_array) == {}

# 测试 is_valid_latitude 函数
def test_is_valid_latitude_valid():
    assert is_valid_latitude(valid_coordinate1[0]) is True

def test_is_valid_latitude_invalid():
    assert is_valid_latitude(invalid_latitude[0]) is False

def test_is_valid_latitude_edge_case():
    assert is_valid_latitude(edge_case_latitude[0]) is True

def test_is_valid_latitude_invalid_type():
    assert is_valid_latitude("abc") is False

# 测试 is_valid_longitude 函数
def test_is_valid_longitude_valid():
    assert is_valid_longitude(valid_coordinate1[1]) is True

def test_is_valid_longitude_invalid():
    assert is_valid_longitude(invalid_longitude[1]) is False

def test_is_valid_longitude_edge_case():
    assert is_valid_longitude(edge_case_longitude[1]) is True
    
def test_is_valid_longitude_invalid_type():
    assert is_valid_longitude("xyz") is False