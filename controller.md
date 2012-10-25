# Controller

## Numpy

    !python

    filtered_max = y_vals <= max_val
    filtered_min = y_vals >= min_val

    filtered_x = numpy.intersect1d(x_vals[filtered_min], x_vals[filtered_max])
    filtered_y = numpy.intersect1d(y_vals[filtered_min], y_vals[filtered_max])

- Arrays with brains

# Presenter Notes

- In-memory
- Written in C/Python

--------------------------------------------------

# Controller

## Pandas

- Fast read/write for SQL dbs, CSV, HDF5
- 'Group by', merge, concatenate large datasets
- Toolkit to unify numpy/matplotlib
- 'Replacement' for R

# Presenter Notes

- Popular in financial industry

--------------------------------------------------

# Controller

## Scipy

- Stats
- Integration
- Matrices
- Linear algebra
