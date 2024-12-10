def calculate_area(x1,y1,x2,y2,x3,y3):
    ''' return area using Heron's forumula '''
    a = side_length(x1,y1,x2,y2)
    b = side_length(x2,y2,x3,y3)
    c = side_length(x3,y3,x1,y1)
    s = (1/2)*(a + b + c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))