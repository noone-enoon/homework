import pytest


def test_triangle_rectangle_area(instance_triangle_valid, instance_rectangle):
    assert instance_triangle_valid.add_area(
        instance_rectangle) == instance_triangle_valid.area + instance_rectangle.area


def test_triangle_circle_area(instance_triangle_valid, instance_circle):
    assert instance_triangle_valid.add_area(
        instance_circle) == instance_triangle_valid.area + instance_circle.area


def test_square_rectangle_area(instance_square, instance_rectangle):
    assert instance_square.add_area(instance_rectangle) == instance_square.area + instance_rectangle.area


def test_is_instance_invalid(instance_square):
    with pytest.raises(ValueError):
        instance_square.add_area(1)
