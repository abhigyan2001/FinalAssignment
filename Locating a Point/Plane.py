class Plane:
    """
    A simple class which can be used to represent general rectangular planes
    
    It contains:
    1. A method to initialize its bounds and its quadrants
    2. A method to find in which of its quadrants a given point lies, and it returns a new object of the same type which represents that quadrant of the plane
    3. A method to return the string representation of its bounds
    4. A method to return the bounds as a list of points (here, points are 1x2 lists)
    """

    def __init__(self, lstx, lsty):
        """
        Initialize the x_min, x_max, y_min, y_max, calculate x_mid and y_mid to make it easier to calculate the quadrants bounds
        """
        self.x_min = lstx[0]
        self.x_max = lstx[1]
        self.y_min = lsty[0]
        self.y_max = lsty[1]
        self.x_mid = (self.x_min+self.x_max)/2
        self.y_mid = (self.y_min+self.y_max)/2
        self.q1 = [[self.x_min,self.x_mid],[self.y_min,self.y_mid]]
        self.q2 = [[self.x_mid,self.x_max],[self.y_min,self.y_mid]]
        self.q3 = [[self.x_mid,self.x_max],[self.y_mid,self.y_max]]
        self.q4 = [[self.x_min,self.x_mid],[self.y_mid,self.y_max]]
    def whichQuadrant(self, point):
        """
        Find which quadrant a given point lies in and return the Plane object representing that
        """
        x = point[0]
        y = point[1]
        if x>=self.x_min and x<self.x_mid:
            if y>=self.y_min and y<self.y_mid:
                return Plane(self.q1[0],self.q1[1])
            elif y>=self.y_mid and y<self.y_max:
                return Plane(self.q4[0],self.q4[1])
        elif x>=self.x_mid and x<self.x_max:
            if y>=self.y_min and y<self.y_mid:
                return Plane(self.q2[0],self.q2[1])
            elif y>=self.y_mid and y<self.y_max:
                return Plane(self.q3[0],self.q3[1])
        else:
            return None
    def __str__(self):
        """
        Return the string representation of the Plane object as the bounding values
        """
        return "x_min = "+str(self.x_min)+", x_max = "+str(self.x_max)+"\ny_min = "+str(self.y_min)+", y_max = "+str(self.y_max)
    def boundingBox(self):
        """
        Return the bounding box of the plane as a list of points, where points are 1x2 lists
        """
        return [[self.x_min,self.y_min],[self.x_min,self.y_max],[self.x_max,self.y_max],[self.x_max,self.y_min]]
