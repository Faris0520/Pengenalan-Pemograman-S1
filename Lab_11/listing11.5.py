import math # need sqrt

class Point(object):
    def __init__(self, x_param = 0.0, y_param = 0.0):
        """Create x and y attributes. Defaults are 0.0"""
        self.x = x_param
        self.y = y_param
    def distance(self, param_pt):
        """Distance between self and a point"""
        x_diff = self.x - param_pt.x # (x1 - x2)
        y_diff = self.y - param_pt.y # (y1 - y2)
        # square differences, sum, and take sqrt
        return math.sqrt(x_diff**2 + y_diff**2)
    
    def sum(self, param_pt):
        """Vector Sum of self and a point return a point instance"""
        new_pt = Point()
        new_pt.x = self.x + param_pt.x
        new_pt.y = self.y + param_pt.y
        return new_pt