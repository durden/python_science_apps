#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import sys

from PyQt4 import QtGui

import view
import model


def main():
    """main"""

    # Convert data then we can interface with pytables exclusively
    model.convert_xls_to_hdf5(model.XLS_FILENAME, model.HDF5_FILENAME)

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    window.setWindowTitle('Sample App')

    month_prod_dialog = view.ProductionByMonthDialog(window)

    x_vals, y_vals = model.production_by_month()
    month_prod_dialog.loadData(x_vals, y_vals)
    month_prod_dialog.show()

    window.setCentralWidget(month_prod_dialog)

    state_prod_dialog = view.StateProductionDialog(window)

    for st in model.STATES:
        x_vals, y_vals = model.production_by_state(st)
        state_prod_dialog.loadData(st, x_vals, y_vals)

    state_prod_dialog.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
