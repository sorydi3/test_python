from Shape import Square,Triangle


def main():
    my_triangle = Triangle(a=3,b=4,c=5)
    print(f"Triangle perimeter is is "
    f"{my_triangle.perimeter()}")
    my_square = Square(3)
    print(f"My square area iiiis  {my_square.area()}")


if __name__ == '__main__':
    main()