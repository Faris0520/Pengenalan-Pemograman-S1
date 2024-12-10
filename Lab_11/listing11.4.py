import math # need sqrt

# a point is a cartesian point (x,y)
# all values are float unless otherwise noted
class Point(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def distance (self, param_pt): # standard distance formula
        """Distance between self and a Point"""
        x_diff = self.x - param_pt.x # (x1-x2)
        y_diff = self.y - param_pt.y # (y1-y2)
        # square differences, sum and take sqrt
        return math.sqrt(x_diff**2 + y_diff**2)
    
    def sum (self, param_pt): # new point from vector sum
        """Vector Sum of self and a Point"""
        new_pt = Point()
        new_pt.x = self.x + param_pt.x
        new_pt.y = self.y + param_pt.y
        return new_pt