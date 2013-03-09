# Controller

## NumPy

- Arrays with brains
- Fast element-wise operations
- Smart memory management/copy semantics

# Presenter Notes

- In-memory
- Written in C/Python

--------------------------------------------------

# Controller

## NumPy

    !python
    >>> x = range(10000)
    >>> %timeit [item + 1 for item in x]
    1000 loops, best of 3: 437 us per loop
    >>> x = numpy.arange(10000)
    >>> %timeit x + 1
    100000 loops, best of 3: 13.9 us per loop

--------------------------------------------------

# Controller

## NumPy

    !python
    >>> x = numpy.arange(3)
    >>> x
    array([0, 1, 2])
    >>> x[x > 1]
    array([2])
    >>> x > 1
    array([False, False,  True], dtype=bool)

--------------------------------------------------

# Controller

## NumPy

    !python
    >>> x[:2][0] = 1
    >>> x
    array([1, 1, 2])
    >>> x[x > 0][0] = 10
    >>> x
    array([1, 1, 2])

- copy vs. view

--------------------------------------------------

# Controller

## Pandas

- Fast read/write for SQL dbs, CSV, HDF5
- 'Group by' and merge large data sets
- Toolkit to unify NumPy/matplotlib
- 'Replacement' for R

# Presenter Notes

- Popular in financial industry

--------------------------------------------------

# Controller

## Pandas

    !python
    >>> import numpy as np
    >>> import pandas as pd
    >>> rand_arr = np.random.rand(2, 2)
    >>> np.savetxt('test.out',
                   rand_arr,
                   delimiter=' ',
                   fmt='%1.5f',
                   header='a b',
                   comments='')
    >>> pd.read_csv('test.out',
                    delim_whitespace=True)
            a        b
    0  0.93954  0.74496
    1  0.12518  0.17269

--------------------------------------------------

# Controller

## Pandas

- File size: 208052 bytes (203.18 kb, 0.20 mb)
- 26 columns
- 1000 rows
- pandas.read_csv: 0.56s
- custom OrderedDict (10 lines): 1.37s
- numpy.loadtxt: 3.29s

--------------------------------------------------

# Controller

## Scipy

- Stats
- Integration
- Matrices
- Linear algebra

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


