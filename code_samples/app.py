#!/usr/bin/env python

"""
Simple app to demonstrate writing an MVC application for oil industry.
"""

import sys

from PyQt4 import QtGui

import view
import model
import controller


def main():
    """main"""

    # Convert data then we can interface with pytables exclusively
    model.convert_xls_to_hdf5(model.XLS_FILENAME, model.HDF5_FILENAME)

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    window.setWindowTitle('PyHOU Sample App')
    window.setCentralWidget(controller.plot_production_by_month())
    window.show()

    state_prod_window = view.StateProductionDialog(
                                        controller.plot_production_by_state(),
                                        window)
    state_prod_window.setWindowTitle('Production by State')
    state_prod_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
