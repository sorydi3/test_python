PRE-REQUISITES
=============

* cython module
* python 2.7 or higher

INSTALLATION
============
* pip install -r requirements.txt

SETUP
=====
* python setup.py build_ext --inplace # to build the cython module in the current directory , this will create a .so file and a .c file

USAGE
=====
```python
 from Shape import Triangle, Square

 square = Square(3)
 print(f'Area of square is {square.area()}')

```

