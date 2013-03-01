# Controller

## Numpy

    !python
    >>> x = range(10000)
    >>> %timeit [item + 1 for item in x]
    1000 loops, best of 3: 437 us per loop
    >>> x = numpy.arange(10000)
    >>> %timeit x + 1
    100000 loops, best of 3: 13.9 us per loop

    >>> x[x > 9990]
    array([9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999])
    >>> x > 9990
    array([False, False, False, ...,  True,  True,  True], dtype=bool)

    >>> x[:10][0] = 1
    >>> x[:10]
    array([1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> x[x < 9990][0] = 5
    >>> x
    array([   1,    1,    2, ..., 9997, 9998, 9999])

- Arrays with brains
- Fast element-wise operations
- Smart memory management/copy semantics

# Presenter Notes

- In-memory
- Written in C/Python

--------------------------------------------------

# Controller

## Pandas

- Fast read/write for SQL dbs, CSV, HDF5
- 'Group by', merge, concatenate large data sets
- Toolkit to unify numpy/matplotlib
- 'Replacement' for R

# Presenter Notes

- Popular in financial industry

--------------------------------------------------

# Controller

## Scipy

    !python
    >>> from scipy import integrate
    >>> x2 = lambda x: x**2
    >>> integrate.quad(x2,0.,4.)
    (21.333333333333332, 2.3684757858670003e-13)
    >>> print 4.**3/3
    21.3333333333

- Stats
- Integration
- Matrices
- Linear algebra
