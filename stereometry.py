import math


def base_formula_1(a, b, c, a1, b1, c1):
    print(abs((a * a1 + b * b1 + c * c1)), (math.sqrt(abs((a * a + b * b + c * c))) * (math.sqrt(abs((a1 * a1 + b1 * b1 + c1 * c1))))))
    return abs((a * a1 + b * b1 + c * c1)) / (math.sqrt(abs((a * a + b * b + c * c))) * (math.sqrt(abs((a1 * a1 + b1 * b1 + c1 * c1)))))


class point:
    def __init__(self, x, y, z, name=None):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def coordinates(self):
        return self.x, self.y, self.z


class line:
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.z = b.z - a.z

    def find_the_angle_between_two_lines(self, li):
        return math.degrees(math.acos(base_formula_1(self.x, self.y, self.z, li.x, li.y, li.z)))

    def find_the_angle_between_line_and_plane(self, pl):
        return math.degrees(math.asin(base_formula_1(self.x, self.y, self.z, pl.a, pl.b, pl.c)))


class plane:
    def __init__(self, fp, sp, tp):

        self.a = (sp.y - fp.y) * (tp.z - fp.z) - (tp.y - fp.y) * (sp.z - fp.z)

        self.b = (tp.x - fp.x) * (sp.z - fp.z) - (sp.x - fp.x) * (tp.z - fp.z)

        self.c = (sp.x - fp.x) * (tp.y - fp.y) - (tp.x - fp.x) * (sp.y - fp.y)

        self.d = -(fp.x * self.a + fp.y * self.b + fp.z * self.c)


    def formula(self):
        return self.a, self.b, self.c, self.d

    def find_the_angle_between_two_planes(self, pl):
        return math.degrees(math.acos(base_formula_1(self.a, self.b, self.c, pl.a, pl.b, pl.c)))

    def find_the_angle_between_plane_and_line(self, li):
        return math.degrees(math.asin(base_formula_1(self.a, self.b, self.c, li.x, li.y, li.z)))
