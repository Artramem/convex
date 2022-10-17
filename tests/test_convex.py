from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Void()

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # При добавлении точки двуугольник может превратиться в другой двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)


class TestPerimeter():

    # Точка
    def test1(self):
        a = Void().add(R2Point(0, 0))
        assert a.perimeter_in_circle() == 0.0

    # Tесты с отрезком

    # Отрезок с концами по разные стороны от большой окружности
    def testoutside(self):
        a = Void().add(R2Point(-3, 0)).add(R2Point(5, 0))
        assert a.perimeter_in_circle() == 4.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside1(self):
        a = Void().add(R2Point(-1, 0)).add(R2Point(5, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside2(self):
        a = Void().add(R2Point(-5, 0)).add(R2Point(-1, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside3(self):
        a = Void().add(R2Point(-1, 0)).add(R2Point(-5, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside4(self):
        a = Void().add(R2Point(-5, 0)).add(R2Point(1, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside5(self):
        a = Void().add(R2Point(5, 0)).add(R2Point(1, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside6(self):
        a = Void().add(R2Point(0, 5)).add(R2Point(0, -1))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами вне большой окружности
    def testoutside7(self):
        a = Void().add(R2Point(0, 5)).add(R2Point(0, -5))
        assert a.perimeter_in_circle() == 4.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside8(self):
        a = Void().add(R2Point(0, 1)).add(R2Point(0, 5))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside9(self):
        a = Void().add(R2Point(0, 1)).add(R2Point(0, -5))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри и вне большой окружности
    def testoutside10(self):
        a = Void().add(R2Point(0, -5)).add(R2Point(0, 1))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами вне большой окружности
    def testoutside11(self):
        a = Void().add(R2Point(0, -5)).add(R2Point(0, -4))
        assert a.perimeter_in_circle() == 0.0

    # Отрезок с концами вне большой окружности
    def testoutside12(self):
        a = Void().add(R2Point(5, 5)).add(R2Point(0, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами вне большой окружности
    def testoutside13(self):
        a = Void().add(R2Point(0, 0)).add(R2Point(5, 5))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами вне большой окружности
    def testoutside14(self):
        a = Void().add(R2Point(0, 0)).add(R2Point(-5, -5))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами вне большой окружности
    def testoutside15(self):
        a = Void().add(R2Point(-5, -5)).add(R2Point(0, 0))
        assert a.perimeter_in_circle() == 2.0

    # Отрезок с концами внутри большой окружности
    def testinside(self):
        a = Void().add(R2Point(0, -1)).add(R2Point(0, 1.5))
        assert a.perimeter_in_circle() == 1.0

    # Отрезок с концами внутри большой окружности
    def testinside1(self):
        a = Void().add(R2Point(0, 2)).add(R2Point(0, -2))
        assert a.perimeter_in_circle() == 4.0

    # Отрезок, лежащий внутри маленькой окружности
    def test2(self):
        a = Void().add(R2Point(-0.5, 0)).add(R2Point(0.5, 0))
        assert a.perimeter_in_circle() == 0.0

    # Отрезок вне большой окружности
    def test3(self):
        a = Void().add(R2Point(3, 0)).add(R2Point(5, 0))
        assert a.perimeter_in_circle() == 0.0

    # Отрезок, лежащий полностью внутри кольца
    def test4(self):
        a = Void().add(R2Point(-1, 1.5)).add(R2Point(1, 1.5))
        assert a.perimeter_in_circle() == 4.0

    # Отрезок, один конец внутри маленького, второй внутри большого
    def test5(self):
        a = Void().add(R2Point(0, 0)).add(R2Point(1.5, 1))
        assert round(a.perimeter_in_circle(), 2) == 1.61

    # Отрезок, один конец внутри маленького, второй внутри большого
    def test51(self):
        a = Void().add(R2Point(1.5, 0)).add(R2Point(0, 0))
        assert a.perimeter_in_circle() == 1.0

    # Отрезок, один конец внутри маленького, второй внутри большого
    def test52(self):
        a = Void().add(R2Point(0, 0)).add(R2Point(-1.5, 0))
        assert a.perimeter_in_circle() == 1.0

    # Отрезок, один конец внутри большой окружности, другой снаружи

    def test6(self):
        a = Void().add(R2Point(1.5, 0)).add(R2Point(3, 0))
        assert a.perimeter_in_circle() == 1

    # Тесты с фигурами

    # Треугольник, все точки внутри кольца,
    # нижняя сторона пересекает маленькую окружность

    def test7(self):
        a = Void().add(
                R2Point(1.5, 0)).add(
                R2Point(-1.5, 0)).add(
                R2Point(0, 1.5))
        assert round(a.perimeter_in_circle(), 2) == 5.24

    # Треугольник, лежащий полностью в кольце
    # (Периметр равен периметру внутри кольца)
    def test8(self):
        a = Void().add(
                R2Point(1.5, 0)).add(
                R2Point(1.6, 0)).add(
                R2Point(1.6, 1))
        assert a.perimeter_in_circle() == a.perimeter()

    # Прямоугольник, нижняя сторона полностью в маленькой окружности
    def test9(self):
        a = Void().add(R2Point(-1, 0)).add(
                R2Point(-1, 1)).add(
                R2Point(1, 1)).add(
                R2Point(1, 0))
        assert a.perimeter_in_circle() == 4.0

    # Прямоугольник вне кольца
    def test10(self):
        a = Void().add(R2Point(-4, -4)).add(
                R2Point(-4, 4)).add(
                R2Point(4, 4)).add(
                R2Point(4, -4))
        assert a.perimeter_in_circle() == 0

    # Фигура, похожая на дом
    def test11(self):
        a = Void().add(R2Point(-1.5, 0)).add(
                R2Point(-1.5, 1)).add(R2Point(0, 2)).add(
                R2Point(1.5, 1)).add(R2Point(1.5, 0))
        assert round(a.perimeter_in_circle(), 2) == 6.61


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon(self):
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3
    #   добавление точки внутрь многоугольника не меняет их количества

    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3
    #   добавление другой точки может изменить их количество

    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4
    #   изменения выпуклой оболочки могут и уменьшать их количество

    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))
    #   добавление точки может его изменить

    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_аrea1(self):
        assert self.f.area() == approx(0.5)
    #   добавление точки может увеличить площадь

    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)
