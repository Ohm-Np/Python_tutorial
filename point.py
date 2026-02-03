#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:08:30 2022

@author: rottmann
"""
import math


class Point:
    """Simple class Point"""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        """Initialization of a point.

        The default values of the x- and y-coordinate are 0."""
        self.__x = x
        self.__y = y

    def getX(self) -> float:
        """Getter method for x."""
        return self.__x

    def getY(self) -> float:
        """Getter method for y."""
        return self.__y

    def setX(self, x: float) -> None:
        """Setter method for x."""
        self.__x = x

    def setY(self, y: float) -> None:
        """Setter method for y."""
        self.__y = y

    def __str__(self) -> str:
        """To-string method for the point class."""
        return "Point(" + str(self.__x) + "," + str(self.__y) + ")"

    def __eq__(self, other) -> bool:
        """Check the equality with another point.

        Two points are equal if their x- and y-coordinates are equal."""
        return self.__x == other.getX() and self.__y == other.getY()

    def translate(self, x: float, y: float) -> None:
        """Translate a point by a specified x and y."""
        self.__x += x
        self.__y += y

    def distance(self, other) -> float:
        """Calculate the distance to another point."""
        return math.sqrt((self.__x - other.getX()) ** 2 + (self.__y - other.getY()) ** 2)


    def clone(self) -> "Point":
        """Create a copy of the point."""
        return Point(self.__x, self.__y)
