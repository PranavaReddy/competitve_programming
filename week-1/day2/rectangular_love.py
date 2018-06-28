import unittest

def find_range_overlap(point1, length1, point2, length2):    
    maximum_startpoint = max(point1, point2)
    minimum_endpoint = min(point1 + length1, point2 + length2)
    
    if maximum_startpoint >= minimum_endpoint:
        return (None, None)  
    overlap_length = minimum_endpoint - maximum_startpoint
    return (maximum_startpoint, overlap_length)


def find_rectangular_overlap(rectangle_1, rectangle_2):
    
    startPoint_x, overlap_width  = find_range_overlap(rectangle_1['left_x'],
                                                         rectangle_1['width'],
                                                         rectangle_2['left_x'],
                                                         rectangle_2['width'])
    startPoint_y, overlap_height = find_range_overlap(rectangle_1['bottom_y'],
                                                         rectangle_1['height'],
                                                         rectangle_2['bottom_y'],
                                                         rectangle_2['height'])    
    if not overlap_width or not overlap_height:
        return 
        {
            'left_x'   : None,
            'bottom_y' : None,
            'width'    : None,
            'height'   : None,
        }

    return
     {
        'left_x'   : startPoint_x,
        'bottom_y' : startPoint_y,
        'width'    : overlap_width,
        'height'   : overlap_height,
    }





# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rectangle_1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rectangle_2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rectangle_1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rectangle_2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rectangle_1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rectangle_2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rectangle_1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rectangle_2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rectangle_1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rectangle_2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rectangle_1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rectangle_2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rectangle_1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rectangle_2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rectangle_1, rectangle_2)
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
