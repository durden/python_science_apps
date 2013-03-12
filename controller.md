# Controller

## NumPy

- Arrays with brains
- Fast element-wise operations
- Smart memory management/copy semantics

# Presenter Notes

- Controller part is where things get exciting, unique to Python
- Base of any scientific app in Python
- Lots of incarnations of an array libraries in Python, NumPy learned from them
- NumPy is everywhere, lots of tools use it directly to avoid intermediate
  data types (pandas/pytables)
- In-memory
- Written in C/Python

--------------------------------------------------

# Controller

## NumPy

### - Pure python
    !python
    >>> x = range(10000)
    >>> %timeit [item + 1 for item in x]
    1000 loops, best of 3: 437 us per loop

### - NumPy
    !python
    >>> x = numpy.arange(10000)
    >>> %timeit x + 1
    100000 loops, best of 3: 13.9 us per loop

# Presenter Notes

- Outsource loops to NumPy/C

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

# Presenter Notes

- Boolean indexing, creates new array
- Operations can be chained to build complex 'queries'

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

# Presenter Notes

- Be mindful of how you index
- NumPy is designed for big data
- Tries to avoid copying

--------------------------------------------------

# Controller

## NumPy

    !python
    >>> rand_arr = np.random.rand(2, 2)
    >>> numpy.savetxt('test.out',
                      rand_arr,
                      delimiter=' ',
                      fmt='%1.5f',
                      header='a b',
                      comments='')

# Presenter Notes

- Create 2D array of random float data
- NumPy is full of useful tools; rand/savetxt
- Can save binary data; only viewable with numpy though
- Saving to txt makes data readable for everyone
- Remember, too many ASCII files? Here it is again!
- Keep this in mind, we'll look at it in a bit

--------------------------------------------------

# Controller

## Pandas

- Fast read/write for SQL dbs, CSV, HDF5
- 'Group by' and merge large data sets
- Toolkit to unify NumPy/matplotlib
- 'Replacement' for R

# Presenter Notes

- Popular in financial industry
- R is open source statistical language
- Built on numpy
- 2 main data structures
    - DataSeries -> 1d array with labels
    - DataFrame -> 2d array like SQL table/spreadsheet

--------------------------------------------------

# Controller

## Pandas

    !python
    >>> pandas.read_csv('test.out',
                        delim_whitespace=True)
            a        b
    0  0.93954  0.74496
    1  0.12518  0.17269

# Presenter Notes

- read_csv reads in a DataFame
- Notice it handles our header line, pretty prints, labels
- Pandas excels and got this right; easy to get existing data in

--------------------------------------------------

# Controller

## Pandas

- File size: 208052 bytes (203.18 kb, 0.20 mb)
- 26 columns
- 1000 rows
- pandas.read_csv: 0.56s
- numpy.loadtxt: 2.35s
- custom OrderedDict (10 lines): 1.4s
- numpy.loadtxt into OrderedDict: 2.65s

# Presenter Notes

- Pandas doesn't just get data in easily; it's fast!
- Lots of recent work to optimize this even more
- Pandas heavily optimizes this with Cython
- Cython is outside of scope, but it's a way to speed up Python with data types

--------------------------------------------------

# Controller

## Scipy

- Stats
- Integration
- Matrices
- Linear algebra

# Presenter Notes

- Scipy is huge collection of tools

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


# Presenter Notes

- Wish I knew about this in my calculus classes!
