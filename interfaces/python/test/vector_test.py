from __future__ import print_function
import numpy as np
import find_ell
import ELL
from testing import Testing

def test_double():
    testing = Testing()

    # empty vector
    e = ELL.DoubleVector()
    np.testing.assert_equal(e.size(), 0)

    # vector from list
    l = [1.1,2.2,3.3,4.4,]
    e = ELL.DoubleVector(l)
    
    np.testing.assert_equal(list(e), l)

    # vector from numpy array
    a = np.array(range(10), dtype=float)
    e = ELL.DoubleVector(a)
    
    np.testing.assert_equal(np.asarray(e), a)

    # conver to numpy using array
    b = np.array(e).ravel()
    np.testing.assert_equal(a, b)

    # copy_from numpy array
    e = ELL.DoubleVector()
    e.copy_from(a)
    np.testing.assert_equal(np.asarray(e), a)

    # convert data types
    a = a.astype(np.float32)
    e = ELL.DoubleVector(a)
    np.testing.assert_equal(np.asarray(e), a)

    # enumerating array
    for i in range(a.shape[0]):
        x = a[i]
        y = e[i]
        np.testing.assert_equal(x, y)

    # auto-ravel numpy arrays
    a = np.ones((10,10), dtype=float)
    a *= range(10)
    e = ELL.DoubleVector(a)
    np.testing.assert_equal(np.asarray(e), a.ravel())
    
    testing.ProcessTest("DoubleVector test", True)

def assert_compare_floats(a, b):
    c = np.array(list(a), dtype=np.float32)
    d = np.array(list(b), dtype=np.float32)
    np.testing.assert_equal(c, d)

def test_float():
    testing = Testing()

    # empty vector
    e = ELL.FloatVector()
    np.testing.assert_equal(e.size(), 0)

    # vector from list of floats
    l = [1.1,2.2,3.3,4.4]
    e = ELL.FloatVector(l)
    
    assert_compare_floats(e, l)

    # vector from numpy array
    a = np.array(range(10), dtype=np.float32)
    e = ELL.FloatVector(a)
    
    np.testing.assert_equal(np.asarray(e), a)

    # convert to numpy using array
    b = np.array(e).ravel()
    np.testing.assert_equal(a, b)

    # copy_from numpy array
    e = ELL.FloatVector()
    e.copy_from(a)
    np.testing.assert_equal(np.asarray(e), a)

    # convert data types
    a = a.astype(np.float)
    e = ELL.FloatVector(a)
    np.testing.assert_equal(np.asarray(e), a)
    
    # enumerating array
    for i in range(a.shape[0]):
        x = a[i]
        y = e[i]
        np.testing.assert_equal(x, y)

    # auto-ravel numpy arrays
    a = np.ones((10,10), dtype=np.float32)
    a *= range(10)
    e = ELL.FloatVector(a)
    np.testing.assert_equal(np.asarray(e), a.ravel())
    
    testing.ProcessTest("FloatVector test", True)


def test():
    test_double()
    test_float()
    return 0

if __name__ == "__main__":
    test()