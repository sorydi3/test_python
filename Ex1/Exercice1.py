from mpmath import zetazero

def f(n):

    return 0.0 if n <= 0 else float(zetazero(n).imag)

"""
Function to find a value 'y' in the range [a, b] using binary search
"""
def find(f, y, a, b) -> int:
    return i_find(f, y, a, b)

"""
Internal function that implements binary search to find 'y' in the range [left, right]
"""
def i_find(f, y, left, right):
    # Calculate the middle point
    mid = (right + left) // 2

    # Calculate 'zz' by evaluating the function 'f' at the middle point
    z = f(mid)

    # If 'z' is equal to 'y', return the middle point 'mid'
    if z == y:
        return mid

    # If 'left' and 'right' are the same, 'y' is not in the range, so return -1
    if left == right:
        return -1

    # If 'y' is greater than 'z', adjust the search range to the right half and recursively call i_find
    if y > z:
        mid = mid + 1
        return i_find(f, y, mid, right)
    
    # If 'y' is less than 'z', adjust the search range to the left half and recursively call i_find
    if y < z:
        mid = mid - 1
        return i_find(f, y, left, mid)


if __name__ == "__main":
    # Calculate the value 'y' by evaluating 'f' at a large 'n' (123456789)
    y = f(123456789)  # value in the range

    z = y + 1e-8  # value not in the range

    # Call the 'find' function to find 'z' in the range [0, 10000000000]
    result2 = find(f, z, 0, 10000000000)

    print(f"RESULT 1: {result2}")
