#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Plutosdr Source
# Generated: Fri Aug 24 18:39:30 2018
# GNU Radio version: 3.7.12.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
from gnuradio import qtgui


class plutosdr_source(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Plutosdr Source")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Plutosdr Source")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "plutosdr_source")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 192000
        self.decimation = decimation = 3
        self.rf_samp_rate = rf_samp_rate = samp_rate * decimation
        self.frequency_offset = frequency_offset = 20e3
        self.frequency = frequency = 435275000
        self.Gain = Gain = 0

        ##################################################
        # Blocks
        ##################################################
        self._frequency_offset_range = Range(-40e3, 40e3, 10, 20e3, 200)
        self._frequency_offset_win = RangeWidget(self._frequency_offset_range, self.set_frequency_offset, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_offset_win)
        self._frequency_tool_bar = Qt.QToolBar(self)
        self._frequency_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._frequency_line_edit = Qt.QLineEdit(str(self.frequency))
        self._frequency_tool_bar.addWidget(self._frequency_line_edit)
        self._frequency_line_edit.returnPressed.connect(
        	lambda: self.set_frequency(int(str(self._frequency_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._frequency_tool_bar)
        self._Gain_tool_bar = Qt.QToolBar(self)
        self._Gain_tool_bar.addWidget(Qt.QLabel('Gain'+": "))
        self._Gain_line_edit = Qt.QLineEdit(str(self.Gain))
        self._Gain_tool_bar.addWidget(self._Gain_line_edit)
        self._Gain_line_edit.returnPressed.connect(
        	lambda: self.set_Gain(eng_notation.str_to_num(str(self._Gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._Gain_tool_bar)
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:20001', 100, False, -1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimation,
                taps=None,
                fractional_bw=None,
        )
        self.pluto_source_0 = iio.pluto_source('ip:192.168.2.1', int(frequency+frequency_offset), rf_samp_rate, 20000000, 0x8000, True, True, True, "manual", Gain, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.pluto_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.zeromq_pub_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "plutosdr_source")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_rf_samp_rate(self.samp_rate * self.decimation)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.set_rf_samp_rate(self.samp_rate * self.decimation)

    def get_rf_samp_rate(self):
        return self.rf_samp_rate

    def set_rf_samp_rate(self, rf_samp_rate):
        self.rf_samp_rate = rf_samp_rate
        self.pluto_source_0.set_params(int(self.frequency+self.frequency_offset), self.rf_samp_rate, 20000000, True, True, True, "manual", self.Gain, '', True)

    def get_frequency_offset(self):
        return self.frequency_offset

    def set_frequency_offset(self, frequency_offset):
        self.frequency_offset = frequency_offset
        self.pluto_source_0.set_params(int(self.frequency+self.frequency_offset), self.rf_samp_rate, 20000000, True, True, True, "manual", self.Gain, '', True)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        Qt.QMetaObject.invokeMethod(self._frequency_line_edit, "setText", Qt.Q_ARG("QString", str(self.frequency)))
        self.pluto_source_0.set_params(int(self.frequency+self.frequency_offset), self.rf_samp_rate, 20000000, True, True, True, "manual", self.Gain, '', True)

    def get_Gain(self):
        return self.Gain

    def set_Gain(self, Gain):
        self.Gain = Gain
        Qt.QMetaObject.invokeMethod(self._Gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.Gain)))
        self.pluto_source_0.set_params(int(self.frequency+self.frequency_offset), self.rf_samp_rate, 20000000, True, True, True, "manual", self.Gain, '', True)


def main(top_block_cls=plutosdr_source, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
