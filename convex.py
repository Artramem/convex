from deq import Deq
from r2point import R2Point
import math
from sympy import *


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)

    def perimeter_in_circle(self):
        return 0.0


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self

    def dist_4(self, r1, r2):
        if (r1 <= 2) and (r2 <= 2):
            return R2Point.dist(self.p, self.q)
        elif(self.p.x == self.q.x):
            x1 = self.p.x
            x2 = self.q.x
            y1 = sqrt(4 - x1**2)
            y2 = -sqrt(4 - x2**2)
            if (min(self.p.y, self.q.y) < y1 < max(self.p.y, self.q.y) and
                    min(self.p.y, self.q.y) < y2 < max(self.p.y, self.q.y)):
                return R2Point.dist(R2Point(x1, y1), R2Point(x2, y2))
            elif (min(self.p.y, self.q.y) < y1 < max(self.p.y, self.q.y)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x1, y1), self.q)
                else:
                    return R2Point.dist(R2Point(x1, y1), self.p)
            elif (min(self.p.y, self.q.y) < y2 < max(self.p.y, self.q.y)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x2, y2), self.q)
                else:
                    return R2Point.dist(R2Point(x2, y2), self.p)
            else:
                return 0.0
        elif (self.p.y == self.q.y):
            y1 = self.p.y
            y2 = self.q.y
            x1 = sqrt(4 - y1**2)
            x2 = -sqrt(4 - y1**2)
            if (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x) and
                    min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                return R2Point.dist(R2Point(x1, y1), R2Point(x2, y2))
            elif (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x1, y1), self.q)
                else:
                    return R2Point.dist(R2Point(x1, y1), self.p)
            elif (min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x2, y2), self.q)
                else:
                    return R2Point.dist(R2Point(x2, y2), self.p)
            else:
                return 0.0
        else:
            xa = self.p.x
            ya = self.p.y
            xb = self.q.x
            yb = self.q.y
            B = xb - xa
            A = yb - ya
            C = ya*(xb - xa) - xa*(yb - ya)
            t1 = -B / A
            t2 = -C / A
            var('y')
            y1, y2 = solveset((t1*y - t2)**2 + y**2 - 4, y, domain=S.Reals)
            x1 = t1*y1 - t2
            x2 = t1*y2 - t2
            if (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x) and
                    min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                return R2Point.dist(R2Point(x1, y1), R2Point(x2, y2))
            elif (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x1, y1), self.q)
                else:
                    return R2Point.dist(R2Point(x1, y1), self.p)
            elif (min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x2, y2), self.q)
                else:
                    return R2Point.dist(R2Point(x2, y2), self.p)
            else:
                return 0.0

    def dist_1(self, r1, r2):
        if (r1 <= 1) and (r2 <= 1):
            return R2Point.dist(self.p, self.q)
        elif(self.p.x == self.q.x):
            x1 = self.p.x
            x2 = self.q.x
            y1 = sqrt(1 - x1**2)
            y2 = -sqrt(1 - x2**2)
            if (min(self.p.y, self.q.y) < y1 < max(self.p.y, self.q.y) and
                    min(self.p.y, self.q.y) < y2 < max(self.p.y, self.q.y)):
                return R2Point.dist(R2Point(x1, y1), R2Point(x2, y2))
            elif (min(self.p.y, self.q.y) < y1 < max(self.p.y, self.q.y)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x1, y1), self.q)
                else:
                    return R2Point.dist(R2Point(x1, y1), self.p)
            elif (min(self.p.y, self.q.y) < y2 < max(self.p.y, self.q.y)):
                if(r1 > 2):
                    return R2Point.dist(R2Point(x2, y2), self.q)
                else:
                    return R2Point.dist(R2Point(x2, y2), self.p)
            else:
                return 0.0
        elif (self.p.y == self.q.y):
            y1 = self.p.y
            y2 = self.q.y
            x1 = sqrt(1 - y1**2)
            x2 = -sqrt(1 - y1**2)
            if (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x) and
                    min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                return R2Point.dist(R2Point(x1, y1), R2Point(x2, y2))
            elif (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x)):
                if(r1 > 1):
                    return R2Point.dist(R2Point(x1, y1), self.q)
                else:
                    return R2Point.dist(R2Point(x1, y1), self.p)
            elif (min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                if(r1 > 1):
                    return R2Point.dist(R2Point(x2, y2), self.q)
                else:
                    return R2Point.dist(R2Point(x2, y2), self.p)
            else:
                return 0.0
        else:
            xa = self.p.x
            ya = self.p.y
            xb = self.q.x
            yb = self.q.y
            B = xb - xa
            A = yb - ya
            C = ya*(xb - xa) - xa*(yb - ya)
            t1 = -B / A
            t2 = -C / A
            var('y')
            y1, y2 = solveset((t1*y - t2)**2 + y**2 - 1, y, domain=S.Reals)
            x1 = t1*y1 - t2
            x2 = t1*y2 - t2
            if (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x) and
                    min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                return R2Point.dist(R2Point(x1, y1), R2Point(x2, y2))
            elif (min(self.p.x, self.q.x) < x1 < max(self.p.x, self.q.x)):
                if(r1 > 1):
                    return R2Point.dist(R2Point(x1, y1), self.q)
                else:
                    return R2Point.dist(R2Point(x1, y1), self.p)
            elif (min(self.p.x, self.q.x) < x2 < max(self.p.x, self.q.x)):
                if(r1 > 1):
                    return R2Point.dist(R2Point(x2, y2), self.q)
                else:
                    return R2Point.dist(R2Point(x2, y2), self.p)
            else:
                return 0.0

    def perimeter_in_circle(self):
        # self.p - 1 точка, self.q - 2
        if (self.p.x == self.q.x):
            d = abs(self.p.x)
        else:
            a = self.p.y - self.q.y
            b = self.q.x - self.p.x
            c = (self.p.x*self.q.y - self.q.x*self.p.y)
            d = abs(c)/(math.sqrt(a*a+b*b))
        r1 = math.sqrt(self.p.x**2 + self.p.y**2)
        r2 = math.sqrt(self.q.x**2 + self.q.y**2)
        if (d >= 2):
            return 0.0
        elif(1 <= d < 2):
            return 2*self.dist_4(r1, r2)
        else:
            dist4 = self.dist_4(r1, r2)
            dist1 = self.dist_1(r1, r2)
            return 2*(dist4 - dist1)


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        tmp = (Void().add(a).add(b).perimeter_in_circle()/2 +
               Void().add(a).add(c).perimeter_in_circle()/2 +
               Void().add(b).add(c).perimeter_in_circle()/2)
        self._perimeter_in_circle = tmp
        self._area = abs(R2Point.area(a, b, c))

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    def perimeter_in_circle(self):
        return self._perimeter_in_circle

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            tmp = Void().add(self.points.first()).add(self.points.last())
            tmp = tmp.perimeter_in_circle()/2
            self._perimeter_in_circle -= tmp
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                tmp = Void().add(p).add(self.points.first())
                tmp = tmp.perimeter_in_circle()/2
                self._perimeter_in_circle -= tmp
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                tmp = Void().add(p).add(self.points.last())
                tmp = tmp.perimeter_in_circle()/2
                self._perimeter_in_circle -= tmp
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            tmp1 = Void().add(t).add(self.points.first())
            tmp1 = tmp1.perimeter_in_circle()/2
            tmp2 = Void().add(t).add(self.points.last())
            tmp2 = tmp2.perimeter_in_circle()/2
            self._perimeter_in_circle += tmp1 + tmp2
            self.points.push_first(t)

        return self


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
