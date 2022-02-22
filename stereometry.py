import math


class point:
    def __init__(self, x, y, z, name=None):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def coordinates(self):
        return self.x, self.y, self.z

    def x(self):
        return self.x

    def y(self):
        return self.y

    def z(self):
        return self.z


class plane:
    def __init__(self, f_p, s_p, t_p):
        self.firstInitPoint = f_p
        self.secondInitPoint = s_p
        self.thirdInitPoint = t_p


        self.a
        self.b
        self.c
        self.d
