#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import sys

from PyQt4 import QtGui, QtCore
import numpy

import view
import model


class Controller(QtCore.QObject):
    """Controller for sample app"""

    def __init__(self):
        """Setup controller"""

        super(Controller, self).__init__()

        self._main_window = view.MainWindow(model.STATES)

        self._main_window.filter_dialog.filter_range.connect(
                                                            self._filter_range)
        self._main_window.filter_dialog.filter_max.connect(self._filter_max)
        self._main_window.filter_dialog.reset_values.connect(self._reset)
        self._main_window.filter_dialog.state_selected.connect(
                                                          self._state_selected)

    def launch(self):
        """Load data/start up"""

        x_vals, y_vals = model.production_by_month()
        self._main_window.month_prod_dialog.loadData(x_vals, y_vals)

        for st in model.STATES:
            x_vals, y_vals = model.production_by_state(st)
            self._main_window.state_prod_dialog.loadData(st, x_vals, y_vals)

        self._main_window.show()

    def _get_filter_state_vals(self, state):
        """Get x/y values for state we are filtering"""

        x_vals, y_vals = model.production_by_state(state)
        return (x_vals, y_vals)

    def _reset(self, state):
        """Reset AK state values to originals"""

        # Use built-in string, not QString
        state = str(state)

        x_vals, y_vals = self._get_filter_state_vals(state)
        self._main_window.state_prod_dialog.loadData(state, x_vals, y_vals)
        self._main_window.filter_dialog.filter_boundaries(numpy.min(y_vals),
                                                             numpy.max(y_vals))

    def _state_selected(self, state):
        """State selected by user"""

        # Use built-in string, not QString
        state = str(state)

        x_vals, y_vals = self._get_filter_state_vals(state)
        self._main_window.filter_dialog.filter_boundaries(numpy.min(y_vals),
                                                             numpy.max(y_vals))

    def _filter_max(self, state, max_val):
        """Filter Ak state max"""

        # Use built-in string, not QString
        state = str(state)

        x_vals, y_vals = self._get_filter_state_vals(state)

        # FIXME: Should sanitize this data in a real application since it comes
        # directly from user...

        # Create true arrays to index with
        filtered_max = y_vals <= max_val

        self._main_window.state_prod_dialog.loadData(state,
                                                     x_vals[filtered_max],
                                                     y_vals[filtered_max])

    def _filter_range(self, state, min_val, max_val):
        """Filter state values supplied range"""

        # Use built-in string, not QString
        state = str(state)

        x_vals, y_vals = self._get_filter_state_vals(state)

        # FIXME: Should sanitize this data in a real application since it comes
        # directly from user...

        # Create boolean arrays to index with
        filtered_max = y_vals <= max_val
        filtered_min = y_vals >= min_val

        filtered_x = numpy.intersect1d(x_vals[filtered_min],
                                       x_vals[filtered_max])
        filtered_y = numpy.intersect1d(y_vals[filtered_min],
                                       y_vals[filtered_max])

        self._main_window.state_prod_dialog.loadData(state, filtered_x,
                                                     filtered_y)

def main():
    """main"""

    # Convert data then we can interface with pytables exclusively
    model.convert_xls_to_hdf5(model.XLS_FILENAME, model.HDF5_FILENAME)

    app = QtGui.QApplication(sys.argv)

    controller = Controller()
    controller.launch()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
