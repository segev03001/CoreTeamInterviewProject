import random
import basicShapes
from multimethods import multimethod
import json
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def asJson(self):
        pass

    @abstractmethod
    def CreatePoints(self, num_points, randomness):
        pass


class Line2D(Shape):
    @multimethod()
    def __init__(self):
        self.point = basicShapes.Point2D()
        self.vector = basicShapes.Vector2D()

    @multimethod(basicShapes.Point2D, basicShapes.Vector2D)
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector

    @multimethod(float, float, float, float)
    def __init__(self, x1, y1, a, b):
        self.point = basicShapes.Point2D(x1, y1)
        self.vector = basicShapes.Vector2D(a, b)

    # overriding abstract method
    def asJson(self):
        Line2DJson = json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)
        return "{\nLine2D:" + Line2DJson + "\n}"

    # overriding abstract method
    def CreatePoints(self, num_points, randomness):
        percent80Points = int(0.8 * num_points)
        percent20Points = num_points - percent80Points
        resultPoints = []
        for num_point in range(percent80Points):
            onLine = random.uniform(0.0, 300.0)
            distance = random.uniform(-1 * randomness, randomness)
            ### L : a + t * V
            newVector = self.vector * onLine
            vectorPoint = newVector.getVectorPoint()
            newPoint = vectorPoint + self.point
            if num_point % 2 == 0:
                newPoint.x = newPoint.x + distance
            if num_point % 3 == 0:
                newPoint.y = newPoint.y + distance
            resultPoints.append(newPoint)
        for num_point in range(percent20Points):
            newPoint = basicShapes.Point2D()
            resultPoints.append(newPoint)
        return resultPoints


class Circle2D(Shape):
    @multimethod()
    def __init__(self):
        self.point = basicShapes.Point2D()
        self.radius = random.uniform(0.0, 50.0)

    @multimethod(basicShapes.Point2D, float)
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

    @multimethod(float, float, float)
    def __init__(self, x1, y1, radius):
        self.point = basicShapes.Point2D(x1, y1)
        self.radius = radius

    # overriding abstract method
    def asJson(self):
        Line2DJson = json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)
        return "{\nCircle2D:" + Line2DJson + "\n}"

    # overriding abstract method
    def CreatePoints(self, num_points, randomness):
        percent80Points = int(0.8 * num_points)
        percent20Points = num_points - percent80Points
        resultPoints = []
        for num_point in range(percent80Points):
            Angle = random.uniform(0.0, 360.0)
            distance = random.uniform(-1 * randomness, randomness)
            ### x = cx + r * cos(a)
            ### y = cy + r * sin(a)
            x = self.point.x + self.radius * math.cos(Angle)
            y = self.point.y + self.radius * math.sin(Angle)
            newPoint = basicShapes.Point2D(x, y)
            if num_point % 2 == 0:
                newPoint.x = newPoint.x + distance
            if num_point % 3 == 0:
                newPoint.y = newPoint.y + distance
            resultPoints.append(newPoint)
        for num_point in range(percent20Points):
            newPoint = basicShapes.Point2D()
            resultPoints.append(newPoint)
        return resultPoints


class Line3D(Shape):
    @multimethod()
    def __init__(self):
        self.point = basicShapes.Point3D()
        self.vector = basicShapes.Vector3D()

    @multimethod(basicShapes.Point3D, basicShapes.Vector3D)
    def __init__(self, point, vector):
        self.point = point
        self.radius = vector

    @multimethod(float, float, float, float, float, float)
    def __init__(self, x1, y1, z1, a, b, c):
        self.point = basicShapes.Point2D(x1, y1, z1)
        self.vector = basicShapes.Vector2D(a, b, c)

    # overriding abstract method
    def asJson(self):
        Line2DJson = json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)
        return "{\nLine3D:" + Line2DJson + "\n}"

    # overriding abstract method
    def CreatePoints(self, num_points, randomness):
        percent80Points = int(0.8 * num_points)
        percent20Points = num_points - percent80Points
        resultPoints = []
        for num_point in range(percent80Points):
            onLine = random.uniform(0.0, 300.0)
            distance = random.uniform(-1 * randomness, randomness)
            ### L : a + t * V
            newVector = self.vector *onLine
            vectorPoint = newVector.getVectorPoint()
            newPoint = vectorPoint + self.point
            if num_point % 2 == 0:
                newPoint.x = newPoint.x + distance
            if num_point % 3 == 0:
                newPoint.y = newPoint.y + distance
            newPoint.z = newPoint.z + distance
            resultPoints.append(newPoint)
        for num_point in range(percent20Points):
            newPoint = basicShapes.Point2D()
            resultPoints.append(newPoint)
        return resultPoints


class Plane3D(Shape):
    @multimethod()
    def __init__(self):
        self.point = basicShapes.Point3D()
        self.vector = basicShapes.Vector3D()

    @multimethod(basicShapes.Point3D, basicShapes.Vector3D)
    def __init__(self, point, vector):
        self.point = point
        self.radius = vector

    @multimethod(float, float, float, float, float, float)
    def __init__(self, x1, y1, z1, a, b, c):
        self.point = basicShapes.Point2D(x1, y1, z1)
        self.vector = basicShapes.Vector2D(a, b, c)

    # overriding abstract method
    def asJson(self):
        Line2DJson = json.dumps(self, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4)
        return "{\nPlane3D:" + Line2DJson + "\n}"

    # overriding abstract method
    def CreatePoints(self, num_points, randomness):
        return []
