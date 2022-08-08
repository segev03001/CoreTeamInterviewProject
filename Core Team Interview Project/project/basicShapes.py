import json
import random
from multimethods import multimethod


class Point2D:
    @multimethod()
    def __init__(self):
        self.x = random.uniform(0.0, 300.0)
        self.y = random.uniform(0.0, 300.0)

    @multimethod(float, float)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        resultPoint = Point2D(self.x + point.x, self.y + point.y)
        return resultPoint

    def __mul__(self, num):
        resultPoint2D = Point2D(num * self.x, num * self.y)
        return resultPoint2D

    def asJson(self):
        Line2DJson = json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)
        return "{\nPoint2D:" + Line2DJson + "\n}"


class Point3D(Point2D):
    @multimethod()
    def __init__(self):
        super().__init__()
        self.z = random.uniform(0.0, 300.0)

    @multimethod(float, float, float)
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __add__(self, point):
        resultPoint3D = Point3D(self.x + point.x, self.y + point.y, self.z + point.z)
        return resultPoint3D

    def __mul__(self, num):
        resultPoint3D = Point3D(num * self.x, num * self.y, num * self.z)
        return resultPoint3D

    def asJson(self):
        Line2DJson = json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)
        return "{\nPoint3D:" + Line2DJson + "\n}"


class Vector2D:
    @multimethod()
    def __init__(self):
        self.point1 = Point2D()

    @multimethod(Point2D)
    def __init__(self, p1):
        self.point1 = p1

    @multimethod(float, float)
    def __init__(self, x1, y1):
        self.point1 = Point2D(x1, y1)

    def getVectorPoint(self):
        resultPoint = self.point1
        return resultPoint

    def __mul__(self, num):
        resultVector = Vector2D(self.point1 * num)
        return resultVector


class Vector3D:
    @multimethod()
    def __init__(self):
        self.point1 = Point3D()

    @multimethod(Point3D)
    def __init__(self, p1):
        self.point1 = p1

    @multimethod(float, float, float)
    def __init__(self, x1, y1, z1):
        self.point1 = Point3D(x1, y1, z1)

    def getVectorPoint(self):
        resultPoint = self.point1
        return resultPoint

    def __mul__(self, num):
        resultVector = Vector3D(self.point1 * num)
        return resultVector
