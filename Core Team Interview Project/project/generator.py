import json
import shapes


def getShape(s):
    if s == 'Line2D':
        newS = shapes.Line2D()
        return newS
    elif s == 'Circle2D':
        newS = shapes.Circle2D()
        return newS
    elif s == 'Line3D':
        newS = shapes.Line3D()
        return newS
    elif s == 'Plane3D':
        newS = shapes.Plane3D()
        return newS


def generator(config_path, output_path, debug=False):
    shapesJason = ""
    pointsJason = ""

    with open(config_path) as f:
        data = json.load(f)
        num_points = data['num_points']
        randomness = data['randomness']
        for shape in (data['shapes']):
            for i in range(data['shapes'][shape]):
                newShape = getShape(shape)
                shapesJason += newShape.asJson()
                newPoints = newShape.CreatePoints(num_points, randomness)
                pointsJason += "{\nshape" + "{0}".format(i) + ":\n"
                for point in newPoints:
                    pointsJason += point.asJson()
                pointsJason += "\n}"

    with open(output_path, "w") as f:
        f.write(shapesJason)
        f.write(pointsJason)

    if debug:
        print(shapesJason)
        print(pointsJason)
