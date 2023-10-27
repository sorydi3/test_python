cdef class Square:
    cdef int side
    def __init__(self, int side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side



cdef class Triangle:
    cdef double a, b, c
    def __init__(self, double a, double b, double c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c