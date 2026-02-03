from point import Point
from typing import Optional, List


class Rectangle:
    """Rectangle class for exercises."""

    __maxId = 0

    def __init__(self, lowerLeft: Optional["Point"] = None, upperRight: Optional["Point"] = None):
        """Constructor of the rectangle.

        lowerLeft and upperRight are optinal parameters. the default-point
        constructor will be used if the points are not specified."""
        # if lowerLeft is None:
        #    lowerLeft = Point()
        # if upperRight is None:
        #    upperRight = Point(1, 1)
        self.__id = Rectangle.__maxId
        Rectangle.__maxId += 1
        self.__lowerLeft = lowerLeft or Point()
        self.__upperRight = upperRight or Point(1.0, 1.0)

    def width(self) -> float:
        """Return the width of the rectangle."""
        return self.__upperRight.getX() - self.__lowerLeft.getX()

    def height(self) -> float:
        """Return the height of the rectangle."""
        return self.__upperRight.getY() - self.__lowerLeft.getY()

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width() * self.height()

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * self.width() + 2 * self.height()

    def scale(self, s: float) -> None:
        """Scale the rectangle by the factor s.

        Lower left coordinate is not changed. Width and Height are increase by
        the factor s by moving the upper right coordinate. The values of s have
        to be greater than 0, otherwise nothing changes."""
        if s > 0:
            self.__upperRight.setX(self.__lowerLeft.getX() + s * self.width())
            self.__upperRight.setY(self.__lowerLeft.getY() + s * self.height())

    def translate(self, tx: float, ty: float) -> None:
        """Translate the rectangle by moving both points."""
        self.__lowerLeft.translate(tx, ty)
        self.__upperRight.translate(tx, ty)
        """
        self.__lowerLeft.setX(self.__lowerLeft.getX() + tx)
        self.__lowerLeft.setY(self.__lowerLeft.getY() + ty)
        self.__upperRight.setX(self.__upperRight.getX() + tx)
        self.__upperRight.setY(self.__upperRight.getY() + ty)
        """

    def cloneRectangle(self) -> "Rectangle":
        """Create a deep copy of the rectangle.

        The points are cloned as well."""
        return Rectangle(self.__lowerLeft.clone(), self.__upperRight.clone())

    def getId(self) -> int:
        """Getter method for id."""
        return self.__id

    def getLowerLeft(self) -> "Point":
        """Getter method for lowerLeft."""
        return self.__lowerLeft

    def getUpperRight(self) -> "Point":
        """Getter method for upperRight."""
        return self.__upperRight

    def setLowerLeft(self, lowerLeft: "Point") -> None:
        """Setter method for lowerLeft."""
        self.__lowerLeft = lowerLeft

    def setUpperRight(self, upperRight: "Point") -> None:
        """Setter method for upperRight"""
        self.__upperRight = upperRight

    def containsPoint(self, point: "Point") -> bool:
        """l) Checks if the point is inside of the rectangle."""
        return (
            point.getX() > self.__lowerLeft.getX()
            and point.getX() < self.__upperRight.getX()
            and point.getY() > self.__lowerLeft.getY()
            and point.getY() < self.__upperRight.getY()
        )


    def computeUpperLeft(self) -> "Point":
        """a) Compute the upper left coodinate of the rectangle."""
        return Point(self.__lowerLeft.getX(), self.__upperRight.getY())

    def computeLowerRight(self) -> "Point":
        """a) Compute the lower right coordinate of the rectangle."""
        return Point(self.__upperRight.getX(), self.__lowerLeft.getY())

    def computePoints(self) -> List["Point"]:
        """b) Computing all coordinates of the rectangle.

        Start with the lower left coordinate and continue anti-clockwise."""
        return [self.__lowerLeft, self.computeLowerRight(), self.__upperRight, self.computeUpperLeft()]


    @classmethod
    def fromWkt(cls, wkt: str) -> "Rectangle":
        """c) Convert a Wkt-string into a rectangle."""
        import re

        split = re.split("[(), ]", wkt)
        x = float(split[2])
        y = float(split[3])
        lowerLeft = Point(x, y)
        x = float(split[8])
        y = float(split[9])
        upperRight = Point(x, y)
        """
        # Get part after left bracket
        split = wkt.split("(")
        # Get part before right bracket
        split = split[-1].split(")")
        # Split the coordinates
        coords = split[0].split(",")
        # Split lowerLeft and upperRight coordinate at spaces
        lowerSplit = coords[0].split()
        upperSplit = coords[2].split()

        # Cast the strings to floats
        x = float(lowerSplit[0])
        y = float(lowerSplit[1])
        lowerLeft = Point(x, y)

        x = float(upperSplit[0])
        y = float(upperSplit[1])
        upperRight = Point(x, y)
        """
        return cls(lowerLeft, upperRight)

    @classmethod
    def readFromFile(cls, filename: str) -> List["Rectangle"]:
        """d) Read rectangles from a Wkt-file."""
        rectangles = []
        with open(filename, "r") as f:
            for line in f:
                rectangles.append(cls.fromWkt(line))
            # [cls.fromWkt(line) for line in f]
        return rectangles

    def toWkt(self) -> str:
        """e) Return a Wkt-string with the four corner coordinates of the rectangle"""
        points = self.computePoints()
        result = "POLYGON(("
        for p in points:
            result += str(p.getX()) + " " + str(p.getY()) + ", "
        result += str(points[0].getX()) + " " + str(points[0].getY()) + "))"
        return result

    @classmethod
    def writeToFile(cls, filename: str, rectangles: List["Rectangle"]) -> None:
        """f) Write a list of rectangles as Wkt-strings to a specified file."""
        with open(filename, "w") as f:
            for r in rectangles:
                f.write(r.toWkt())
                f.write("\n")


    def __str__(self) -> str:
        """Default string method."""
        return (
            "Rectangle: (Id: "
            + str(self.__id)
            + ", LowerLeft: "
            + str(self.__lowerLeft)
            + ", UpperRight: "
            + str(self.__upperRight)
            + ")"
        )
