if __name__ == '__main__':
  raise RuntimeError("This module is intended only for import.")

def check_equal(a, b, precision = 0.001):
    is_equal = abs(a - b) < precision
    return is_equal
