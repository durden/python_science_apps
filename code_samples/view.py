"""
View portion of sample app
"""

import datetime

from PyQt4 import Qt, QtGui, QtCore
import PyQt4.Qwt5 as Qwt


class TimeScaleDraw(Qwt.QwtScaleDraw):
    """Scale to display time values in month/year"""

    def label(self, value):
        """
        Convert time value into string-friendly label to be placed on a plot
        """

        super(TimeScaleDraw, self).label(value)

        date = datetime.datetime.fromtimestamp(value)
        return Qwt.QwtText((date.strftime("%b/%Y")))


class ProductionByMonthDialog(QtGui.QDialog):
    """Dialog to plot oil production by month"""

    def __init__(self, parent):
        """init"""

        super(ProductionByMonthDialog, self).__init__(parent)

        self._plot = Qwt.QwtPlot()

        self._plot.setTitle("Oil Production for USA by Month")
        self._plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
        self._plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")

        self._curve = Qwt.QwtPlotCurve("Barrels (in thousands)")
        self._curve.attach(self._plot)

        # Need custom scale to set labels to month/year
        self._plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

        hlayout = QtGui.QHBoxLayout()
        hlayout.setMargin(0)
        hlayout.addWidget(self._plot)

        self.setLayout(hlayout)
        self.setWindowTitle('Production by month')

    def loadData(self, x_vals, y_vals):
        """Load data into plot"""

        self._curve.setData(x_vals, y_vals)
        self._plot.replot()


class FilterAkProductionDialog(QtGui.QDialog):
    """Dialog to filter ak production data in/out"""

    filter_range = QtCore.pyqtSignal(float, float)
    filter_max = QtCore.pyqtSignal(float)
    reset_values = QtCore.pyqtSignal()

    def __init__(self, parent):
        """init"""

        super(FilterAkProductionDialog, self).__init__(parent)

        self._min_label = QtGui.QLabel('Min')
        self._max_label = QtGui.QLabel('Max')
        self._min_txtbox = QtGui.QLineEdit('')
        self._max_txtbox = QtGui.QLineEdit('')

        vlayout = QtGui.QVBoxLayout()

        hlayout = QtGui.QHBoxLayout()
        hlayout.addWidget(self._min_label)
        hlayout.addWidget(self._min_txtbox)
        vlayout.addLayout(hlayout)

        hlayout = QtGui.QHBoxLayout()
        hlayout.addWidget(self._max_label)
        hlayout.addWidget(self._max_txtbox)
        vlayout.addLayout(hlayout)

        # NOTE: PyQwt has some nice built-in widgets that matplotlib doesn't
        self._slider = Qwt.QwtSlider(self, Qt.Qt.Horizontal,
                                     Qwt.QwtSlider.BottomScale)
        self._slider.valueChanged.connect(self._slider_changed)

        vlayout.addWidget(self._slider)

        btn_flags = (QtGui.QDialogButtonBox.Save | QtGui.QDialogButtonBox.Reset)
        button_box = QtGui.QDialogButtonBox(btn_flags)
        button_box.accepted.connect(self.save)
        button_box.button(Qt.QDialogButtonBox.Reset).clicked.connect(
                                                        self.reset_values.emit)
        vlayout.addWidget(button_box)

        self.setLayout(vlayout)
        self.setWindowTitle('Filter Ak production')
        self.setMinimumHeight(240)
        self.setMinimumWidth(480)

    def _slider_changed(self, val):
        """Slide changed to given val"""

        self.filter_max.emit(val)

    def filter_boundaries(self, min_val, max_val):
        """Setup the filter boundaries"""

        self._min_txtbox.setText(str(min_val))
        self._max_txtbox.setText(str(max_val))
        self._slider.setRange(min_val, max_val)
        # Show everything by default and filter from max to min
        self._slider.setValue(max_val)

    def save(self):
        """Filter values"""

        # FIXME: Should handle users entering data that cannot be converted to
        # float here
        self.filter_range.emit(float(self._min_txtbox.text()),
                                float(self._max_txtbox.text()))


class StateProductionDialog(QtGui.QDialog):
    """Plot production by state"""

    def __init__(self, parent):
        """init"""

        super(StateProductionDialog, self).__init__(parent)

        self._plot = Qwt.QwtPlot()

        self._plot.setTitle("Oil Production by State")
        self._plot.setAxisTitle(Qwt.QwtPlot.xBottom, "Date")
        self._plot.setAxisTitle(Qwt.QwtPlot.yLeft, "Barrels (in thousands)")
        self._plot.insertLegend(Qwt.QwtLegend())

        # Need custom scale to set labels to month/year
        self._plot.setAxisScaleDraw(Qwt.QwtPlot.xBottom, TimeScaleDraw())

        self._la_curve = create_curve('La', QtCore.Qt.green)
        self._ca_curve = create_curve('Ca', QtCore.Qt.black)
        self._tx_curve = create_curve('Tx', QtCore.Qt.blue)
        self._ak_curve = create_curve('Ak', QtCore.Qt.red)

        self._la_curve.attach(self._plot)
        self._ca_curve.attach(self._plot)
        self._tx_curve.attach(self._plot)
        self._ak_curve.attach(self._plot)

        vlayout = QtGui.QVBoxLayout()
        vlayout.setMargin(0)
        vlayout.addWidget(self._plot)

        self.setLayout(vlayout)
        self.setWindowTitle('Oil production by state')

    def loadData(self, state_abbr, x_vals, y_vals):
        """Load data into plot"""

        if state_abbr == 'la':
            self._la_curve.setData(x_vals, y_vals)
        elif state_abbr == 'tx':
            self._tx_curve.setData(x_vals, y_vals)
        elif state_abbr == 'ak':
            self._ak_curve.setData(x_vals, y_vals)
        elif state_abbr == 'ca':
            self._ca_curve.setData(x_vals, y_vals)
        else:
            raise ValueError('Invalid state')

        self._plot.replot()


def create_curve(title, color):
    """Helper to create a new curve with given data and color"""

    curve = Qwt.QwtPlotCurve(title)
    curve.setPen(QtGui.QPen(color))
    curve.setCurveType(Qwt.QwtPlotCurve.Yfx)
    curve.setStyle(Qwt.QwtPlotCurve.Lines)

    return curve
